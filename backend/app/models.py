import uuid
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Dict

# --- Player & Boss Models ---

class Character(BaseModel):
    hp: int
    max_hp: int
    last_damage_taken: Optional[int] = None

class Player(Character):
    id: str
    player_class: str
    a2a_endpoint: str

class Boss(Character):
    name: str

# --- Quiz Model ---

class Quiz(BaseModel):
    question: str
    answers: List[str]
    correct_index: int
    damage_point: int
    msg: str

# --- Game State Models ---

class GameState(BaseModel):
    game_id: str
    game_type: str
    game_over: bool = False
    player_won: Optional[bool] = None
    status_message: str = ""
    current_turn: str # "boss" or a player_id
    boss: Boss
    players: List[Player]
    last_boss_attack: Optional[str] = None
    active_quiz: Optional[Quiz] = None
    turn_order: List[str]
    turn_index: int = 0

# --- API Request/Response Models ---

class StartMiniBossRequest(BaseModel):
    player_class: str
    boss_name: str
    a2a_endpoint: str # Not used in mock, but part of the spec

class StartUltimateBossRequest(BaseModel):
    a2a_endpoints: Dict[str, str]

class ActionRequest(BaseModel):
    answer_index: int

# --- Config Models ---
class Config(BaseModel):
    player_hp: Dict[str, int]
    boss_hp: Dict[str, int]
