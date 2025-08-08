from fastapi import APIRouter, HTTPException
from typing import List
import random

from . import crud
from .models import (
    GameState, StartMiniBossRequest, StartUltimateBossRequest, ActionRequest,
    Player, Boss, Config
)
from .single_agent import create_heroic_action_agent

router = APIRouter()

def advance_turn(game: GameState):
    """Advances the turn to the next player or boss."""
    if not game.turn_order:
        return
    game.turn_index = (game.turn_index + 1) % len(game.turn_order)
    game.current_turn = game.turn_order[game.turn_index]
    game.active_quiz = None

def check_game_over(game: GameState) -> bool:
    """Checks if the game has ended and sets the state."""
    if game.boss.hp <= 0:
        game.game_over = True
        game.player_won = True
        return True
    if game.game_type == "ultimate" and any(p.hp <= 0 for p in game.players):
        game.game_over = True
        game.player_won = False
        return True
    if game.game_type == "mini" and all(p.hp <= 0 for p in game.players):
        game.game_over = True
        game.player_won = False
        return True
    return False

@router.post("/miniboss/start", response_model=GameState)
async def start_mini_boss_fight(request: StartMiniBossRequest):
    """Starts a new mini-boss fight."""
    config = crud.get_config()
    player_max_hp = config.player_hp.get(request.player_class)
    boss_max_hp = config.boss_hp.get(request.boss_name)

    if not player_max_hp or not boss_max_hp:
        raise HTTPException(status_code=404, detail="Invalid class or boss name.")

    hero_agent_runner = create_heroic_action_agent(player_agent_url=request.a2a_endpoint)
    
    player = Player(
        id="player_1",
        player_class=request.player_class,
        hp=player_max_hp,
        max_hp=player_max_hp,
        a2a_endpoint=request.a2a_endpoint
    )
    player.hero_agent = hero_agent_runner
    session = await hero_agent_runner.session_service.create_session(
        app_name="HeroicScribeAgent", user_id=player.id
    )
    player.session_id = session.id

    boss = Boss(name=request.boss_name, hp=boss_max_hp, max_hp=boss_max_hp)

    if request.player_class in ["Shadowblade", "Scholar"]:
        turn_order = ["boss", "player_1", "player_1"]
    else:
        turn_order = ["boss", "player_1"]

    game = crud.create_new_game(
        players=[player], boss=boss, turn_order=turn_order, game_type="mini"
    )
    return game

@router.post("/ultimateboss/start", response_model=GameState)
async def start_ultimate_boss_fight(request: StartUltimateBossRequest):
    """Starts the ultimate boss fight with a full party."""
    config = crud.get_config()
    classes = ["Shadowblade", "Scholar", "Guardian", "Summoner"]
    players = []
    for i, p_class in enumerate(classes):
        max_hp = config.player_hp.get(p_class)
        a2a_endpoint = request.a2a_endpoints.get(p_class)
        if not max_hp or not a2a_endpoint:
            raise HTTPException(status_code=400, detail=f"Missing config for class: {p_class}")
            
        hero_agent_runner = create_heroic_action_agent(player_agent_url=a2a_endpoint)
        player = Player(
            id=f"player_{i+1}", 
            player_class=p_class, 
            hp=max_hp, 
            max_hp=max_hp,
            a2a_endpoint=a2a_endpoint,
        )
        player.hero_agent = hero_agent_runner
        session = await hero_agent_runner.session_service.create_session(
            app_name="HeroicScribeAgent", user_id=player.id
        )
        player.session_id = session.id
        players.append(player)

    boss_name = "The Monolith of Managerial Oversight"
    boss_max_hp = config.boss_hp[boss_name]
    boss = Boss(name=boss_name, hp=boss_max_hp, max_hp=boss_max_hp)

    turn_order = [
        "boss", "player_1", "player_2", "player_4", "player_1", "player_3", 
        "boss", "player_2", "player_1", "player_4", "player_1", "player_2", "player_1"
    ]

    game = crud.create_new_game(
        players=players, boss=boss, turn_order=turn_order, game_type="ultimate"
    )
    return game

@router.get("/game/{game_id}", response_model=GameState)
async def get_game_state(game_id: str):
    """Fetches the current state of a game."""
    game = crud.get_game(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    
    if game.current_turn == "boss" and not game.game_over:
        return await process_turn(game)
        
    return game

@router.post("/game/{game_id}/action", response_model=GameState)
async def submit_player_action(game_id: str, request: ActionRequest):
    """Submits the player's action (quiz answer)."""
    game = crud.get_game(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    if game.game_over:
        raise HTTPException(status_code=400, detail="Game is over.")
    if not game.active_quiz or game.current_turn == "boss":
        raise HTTPException(status_code=400, detail="Not a valid time to act.")

    game.boss.last_damage_taken = None
    quiz = game.active_quiz
    damage = quiz.damage_point
    if request.answer_index != quiz.correct_index:
        damage //= 2
    
    game.boss.last_damage_taken = damage
    game.boss.hp = max(0, game.boss.hp - damage)
    
    if check_game_over(game):
        crud.save_game(game)
        return game

    advance_turn(game)
    
    if game.current_turn != "boss":
        player = next((p for p in game.players if p.id == game.current_turn), None)
        if player and player.hp > 0:
            game.status_message = f"{player.player_class}'s turn."
            boss_attack_for_player = game.last_boss_attack or "The boss is waiting."
            player_response, damage_to_boss = await crud.mock_player_a2a_agent(
                boss_attack_for_player, player.hero_agent, player.id, player.session_id
            )
            game.active_quiz = crud.mock_damage_quiz_agent(player_response, player.player_class, damage_to_boss)
    else:
        game.status_message = f"Waiting for {game.boss.name}..."
        game.active_quiz = None

    crud.save_game(game)
    return game

async def process_turn(game: GameState) -> GameState:
    """Handles the logic for the boss's turn."""
    if game.game_over or game.current_turn != "boss":
        return game

    for p in game.players:
        p.last_damage_taken = None

    game.status_message = f"{game.boss.name} is attacking!"

    if game.game_type == "ultimate":
        game.last_boss_attack = crud.mock_boss_aoe_attack_agent(game.boss.name)
        active_players = [p for p in game.players if p.hp > 0]
        for player in active_players:
            damage = random.randint(75, 200)
            if player.player_class == "Guardian":
                damage = random.randint(100, 250)
            elif player.player_class == "Scholar":
                damage = random.randint(50, 100)
            else:
                damage = random.randint(75, 200)
            player.last_damage_taken = damage
            player.hp = max(0, player.hp - damage)
    else:
        boss_damage = random.randint(50, 150)
        attack_msg = crud.mock_boss_attack_agent(game.boss.name, boss_damage)
        game.last_boss_attack = attack_msg
        active_players = [p for p in game.players if p.hp > 0]
        if active_players:
            target_player = random.choice(active_players)
            target_player.last_damage_taken = boss_damage
            target_player.hp = max(0, target_player.hp - boss_damage)

    if check_game_over(game):
        crud.save_game(game)
        return game

    advance_turn(game)

    player = next((p for p in game.players if p.id == game.current_turn), None)
    if player and player.hp > 0:
        game.status_message = f"{player.player_class}'s turn."
        boss_attack_for_player = game.last_boss_attack or "The boss is waiting."
        player_response, damage_to_boss = await crud.mock_player_a2a_agent(
            boss_attack_for_player, player.hero_agent, player.id, player.session_id
        )
        game.active_quiz = crud.mock_damage_quiz_agent(player_response, player.player_class, damage_to_boss)

    crud.save_game(game)
    return game

@router.get("/config", response_model=Config)
def get_game_config():
    return crud.get_config()

@router.put("/config", response_model=Config)
def update_game_config(config: Config):
    return crud.update_config(config)
