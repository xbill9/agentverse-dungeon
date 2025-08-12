import uuid
from pydantic import BaseModel, Field, ConfigDict, PrivateAttr
from typing import List, Optional, Dict, Any

# --- Player & Boss Models ---

class Character(BaseModel):
    hp: int
    max_hp: int
    last_damage_taken: Optional[int] = None

class Player(Character):
    id: str
    player_class: str
    a2a_endpoint: str
    _hero_agent: PrivateAttr = PrivateAttr(default=None)
    _agent_runner: PrivateAttr = PrivateAttr(default=None)
    _session_id: PrivateAttr = PrivateAttr(default=None)

    @property
    def hero_agent(self):
        return self._hero_agent

    @hero_agent.setter
    def hero_agent(self, agent: Any):
        self._hero_agent = agent

    @property
    def agent_runner(self):
        return self._agent_runner

    @agent_runner.setter
    def agent_runner(self, runner: Any):
        self._agent_runner = runner

    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, session_id: str):
        self._session_id = session_id

class Boss(Character):
    name: str
    dialog_phrases: List[str] = Field(default_factory=list)

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
    a2a_endpoint: str = "https://summoner-agent-69500317010.us-central1.run.app"

class StartUltimateBossRequest(BaseModel):
    a2a_endpoints: Dict[str, str]

class ActionRequest(BaseModel):
    answer_index: int

# --- Config Models ---
class Config(BaseModel):
    player_hp: Dict[str, int]
    boss_hp: Dict[str, int]
