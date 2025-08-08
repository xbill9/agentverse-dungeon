import random
import uuid
from typing import Dict, Optional

from .models import GameState, Player, Boss, Quiz, Config
from .shadowblade_quizzes import shadowblade_quizzes
from .scholar_quizzes import scholar_quizzes
from .guardian_quizzes import guardian_quizzes
from .summoner_quizzes import summoner_quizzes
from .single_agent import process_player_action

# In-memory "database"
game_db: Dict[str, GameState] = {}

# Default configuration, can be updated via API
GAME_CONFIG = Config(
    player_hp={
        "Shadowblade": 500,
        "Scholar": 450,
        "Guardian": 650,
        "Summoner": 400,
    },
    boss_hp={
        "Procrastination": 1000,
        "Hype": 800,
        "Dogma": 1200,
        "Legacy": 1500,
        "Perfectionism": 900,
        "Obfuscation": 1100,
        "Apathy": 700,
        "The Monolith of Managerial Oversight": 5000,
    }
)

BOSS_WEAKNESSES = {
    "Procrastination": "Inescapable Reality",
    "Hype": "Inescapable Reality",
    "Dogma": "Revolutionary Rewrite",
    "Legacy": "Revolutionary Rewrite",
    "Perfectionism": "Elegant Sufficiency",
    "Obfuscation": "Elegant Sufficiency",
    "Apathy": "Unbroken Collaboration",
    "The Monolith of Managerial Oversight": [
        "Inescapable Reality", "Revolutionary Rewrite",
        "Elegant Sufficiency", "Unbroken Collaboration"
    ]
}

# --- Game State Management ---

def get_game(game_id: str) -> Optional[GameState]:
    return game_db.get(game_id)

def save_game(game: GameState):
    game_db[game.game_id] = game

def create_new_game(players: list, boss: Boss, turn_order: list, game_type: str) -> GameState:
    game_id = str(uuid.uuid4())
    game = GameState(
        game_id=game_id,
        game_type=game_type,
        current_turn="boss",
        boss=boss,
        players=players,
        turn_order=turn_order,
        turn_index=0,
    )
    save_game(game)
    return game

# --- Config Management ---

def get_config() -> Config:
    return GAME_CONFIG

def update_config(new_config: Config) -> Config:
    global GAME_CONFIG
    GAME_CONFIG = new_config
    return GAME_CONFIG

# --- Mock Agent Calls ---

def mock_boss_attack_agent(boss_name: str, damage: int) -> str:
    """Generates a creative attack message including the boss's weakness and damage."""
    weakness = BOSS_WEAKNESSES[boss_name]
    if isinstance(weakness, list):
        weakness = random.choice(weakness)
    
    attack_templates = [
        f"{boss_name} looms, its very presence an attack. It whispers of the {weakness} you cannot face, dealing {damage} damage.",
        f"A wave of power emanates from {boss_name}, fueled by your fear of {weakness}. It will hit for {damage} damage.",
        f"The air crackles. {boss_name} declares, 'You will never achieve {weakness}!' as it prepares an attack for {damage} damage.",
    ]
    return random.choice(attack_templates)

def mock_boss_aoe_attack_agent(boss_name: str) -> str:
    """Generates a creative area-of-effect attack message."""
    attack_templates = [
        f"{boss_name} unleashes a wave of despair, striking all challengers.",
        f"A crushing weight descends as {boss_name} attacks the entire party.",
        f"{boss_name} radiates an aura of pure dread, damaging everyone.",
    ]
    return random.choice(attack_templates)

async def mock_player_a2a_agent(boss_attack: str, agent_runner: any, player_id: str):
    """Player's agent responding to the boss and determining damage."""
    print(f"--- Starting New Adventure (User ID: {player_id}) ---")

    # --- First Turn ---
    print("\n--- Turn 1: Attacking ---")
    print(f"Boss Attack: {boss_attack}")
    msg, dmg = await process_player_action(agent_runner, boss_attack, player_id)
    print("\n--- Parsed Result ---")
    print(f"Log: {msg}")
    print(f"Damage: {dmg}")
    return msg, dmg


def mock_damage_quiz_agent(player_response: str, player_class: str, damage_to_boss: int) -> Quiz:
    """Generates a quiz and damage based on the player's (mocked) response and class."""
    class_quizzes = {
        "Shadowblade": shadowblade_quizzes,
        "Scholar": scholar_quizzes,
        "Guardian": guardian_quizzes,
        "Summoner": summoner_quizzes,
    }
    
    questions = class_quizzes.get(player_class, [])
    if not questions:
        # Fallback to a generic quiz if class-specific quizzes are not found
        questions = [
            {
                "question": "What is 2 + 2?",
                "answers": ["3", "4", "5"],
                "correct_index": 1,
            },
            {
                "question": "What is the color of the sky?",
                "answers": ["Blue", "Green", "Red"],
                "correct_index": 0,
            },
            {
                "question": "Which of these is a primary color?",
                "answers": ["Orange", "Green", "Yellow"],
                "correct_index": 2,
            },
        ]
    
    selected_quiz = random.choice(questions)
    
    return Quiz(
        **selected_quiz,
        damage_point=damage_to_boss,
        msg=f"The player prepares a powerful, well-reasoned counter-attack! {player_response}"
    )
