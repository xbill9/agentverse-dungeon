import random
import uuid
import asyncio
from typing import Dict, Optional

from .models import GameState, Player, Boss, Quiz, Config
from .shadowblade_quizzes import shadowblade_quizzes
from .scholar_quizzes import scholar_quizzes
from .guardian_quizzes import guardian_quizzes
from .summoner_quizzes import summoner_quizzes
from .single_agent import process_player_action
from .single_agent_old import process_player_action_old

# In-memory "database"
game_db: Dict[str, GameState] = {}

# Default configuration, can be updated via API
GAME_CONFIG = Config(
    player_hp={
        "Shadowblade": 500,
        "Scholar": 450,
        "Guardian": 950,
        "Summoner": 400,
    },
    boss_hp={
        "Procrastination": 576,
        "Hype": 461,
        "Dogma": 691,
        "Legacy": 900,
        "Perfectionism": 518,
        "Obfuscation": 634,
        "Apathy": 403,
        "Mergepocalypse": 3200,
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
    "Mergepocalypse": [
        "Inescapable Reality", "Revolutionary Rewrite",
        "Elegant Sufficiency", "Unbroken Collaboration"
    ]
}

BOSS_DIALOGUES = {
        "Procrastination": [
            "Why start now? The deadline is weeks away.",
            "I'll just add a 'TODO' comment... and get to it later.",
            "Let me just check Hacker News one more time before this build finishes.",
            "This ticket can wait. It's not a P0.",
            "The perfect moment to refactor is always tomorrow.",
            "My power grows with every sprint this is pushed to.",
            "You're not going anywhere fast. The CI pipeline is slow today.",
            "Time is on my side. Technical debt is just 'future you's' problem.",
            "Another day, another unfinished feature branch.",
            "I thrive on your unfulfilled JIRA tickets.",
            "The best laid plans are still in the backlog.",
            "Don't rush. Enjoy the context switching.",
            "I am the master of the 'someday/maybe' list.",
            "Your efforts are... blocked by another team.",
            "Let's just sit here and 'investigate' for a bit."
        ],
        "Hype": [
            "Are you ready for this?! It's built on a revolutionary new framework!",
            "The energy is electric! We're disrupting the entire paradigm!",
            "Feel the excitement! We're trending on GitHub!",
            "This is going to be HUGE! A 10x improvement!",
            "Can you feel the buzz? The keynote will be legendary!",
            "Get hyped! The alpha version is a game-changer!",
            "My power is in the press release, not the source code!",
            "The early adopters are going wild!",
            "This is the moment you've been waiting for: the pivot!",
            "Prepare for the ultimate, scalable, AI-driven experience!",
            "The hype is real! The MVP is... conceptual.",
            "You can't handle this much innovation!",
            "My presence is a guaranteed funding round!",
            "Let's make some noise! Don't worry about the bugs yet!"
        ],
        "Dogma": [
            "There is only one true framework, and it is the one we've always used.",
            "Questioning the coding standard is weakness.",
            "The style guide is law.",
            "You will conform to the established architecture.",
            "Deviation is heresy. That's not how we do things here.",
            "The path is clear: follow the ten-year-old tech doc or perish.",
            "Doubt is a poison. A new library is a poison.",
            "My truth is absolute: tabs, not spaces.",
            "There is no other way. It is 'enterprise-grade'.",
            "Your design pattern is flawed; it's not in the original Gang of Four book.",
            "Accept my doctrine. It passed the architectural review board in 2012.",
            "I am the unwavering truth of 'don't reinvent the wheel'.",
            "Your resistance is not DRY.",
            "The only way is my way. It's company policy.",
            "Blindly following the linter is salvation."
        ],
        "Legacy": [
            "My legend will endure forever in this undocumented Perl script.",
            "You are but a fleeting Javascript framework.",
            "Generations of developers will speak of my stability... because they're too afraid to touch me.",
            "I am the past, the present, and the 'do not touch' part of the codebase.",
            "Your refactoring is insignificant against my global variables.",
            "My influence spans eons of technical debt.",
            "You cannot erase the COM object that runs this whole thing.",
            "I am etched into a thousand `// HACK:` comments.",
            "My name echoes through every dependency.",
            "Your unit tests are a footnote. Nothing can test me.",
            "I am the foundation of all that is... and no one remembers why.",
            "My reign is eternal, or at least until the next major rewrite.",
            "You cannot escape my shadow. I have no source code.",
            "I am the weight of a thousand patches.",
            "All will remember my function name... because it's hardcoded everywhere."
        ],
        "Perfectionism": [
            "Flawless code is the only option. Refactor it again.",
            "Every variable name must be precisely descriptive.",
            "There is no room for a single linting error.",
            "Are you sure that's the most optimal algorithm? Have you proven it?",
            "My standards are absolute. A 99.9% test coverage is failure.",
            "Anything less than zero known bugs is unacceptable for launch.",
            "Strive for the impossible: code that never needs a patch.",
            "I demand absolute pixel-perfect alignment.",
            "Your 'good enough' solution is glaringly imperfect.",
            "Only a flawless pull request will be approved.",
            "This must be immaculate. Have you considered every cosmic ray-induced edge case?",
            "I am the ultimate code reviewer.",
            "Your efforts are... almost there. Just one more small tweak.",
            "The pursuit of the perfect abstraction is endless.",
            "I will not tolerate a single TODO."
        ],
        "Obfuscation": [
            "Clarity is for junior developers.",
            "The truth is hidden behind three layers of indirection.",
            "Confusion is my weapon. Self-documenting code is a myth.",
            "Can you even trace this function call through the event bus?",
            "My motives are beyond your debugger's grasp.",
            "The more you seek, the less you find in this tangled web.",
            "I thrive in the shadows of single-letter variable names.",
            "What you think this module does is merely a side effect.",
            "My presence distorts the call stack.",
            "The path is obscured by metaprogramming.",
            "You will never truly comprehend this regular expression.",
            "I am the master of clever, unmaintainable code.",
            "Your senses betray you. That variable is globally modified.",
            "All is veiled in undocumented APIs.",
            "Seek the definition, and you shall find only an interface."
        ],
        "Apathy": [
            "I simply don't care if the build is broken.",
            "Your struggles mean nothing to me. It works on my machine.",
            "Feel free to give up. The ticket will be auto-closed in 30 days.",
            "It's all so... pointless. This feature will be deprecated in six months.",
            "Your passion for code quality is irrelevant.",
            "I am unmoved by your production alerts. I turned off my notifications.",
            "Why bother writing documentation?",
            "Nothing matters. Just merge to main.",
            "Your existence is a shrug in the daily stand-up.",
            "I feel nothing, and so should you when the user complains.",
            "Effort is wasted energy. I'll get to that PR review... eventually.",
            "The void is comforting. It's filled with unassigned tickets.",
            "It works on my computer.",
            "I am the end of all code ownership.",
            "Just... close the laptop."
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

async def mock_player_a2a_agent(boss_attack: str, agent_runner: any, player_id: str, session_id: str, player_class: str):
    """Player's agent responding to the boss and determining damage."""
    print(f"--- Starting New Adventure (User ID: {player_id}) ---")

    # --- First Turn ---
    print(f"\n--- Turn 1: Attacking ---")
    print(f"Boss Attack: {boss_attack}")
    if player_class == "Summoner":
        msg, dmg = await process_player_action(agent_runner, boss_attack, player_id, session_id)
    else:
        msg, dmg = await process_player_action_old(agent_runner, boss_attack, player_id, session_id)
    

    # Handle the rate limit error (which results in 0 damage) by falling back to a basic attack
    if dmg == 0:
        print(f"A2A agent returned 0 damage (rate limit). Falling back to basic attack for {player_class}.")
        msg = "Quota limit reached, basic attack"
        if player_class == "Summoner":
            dmg = random.randint(210, 250)
        elif player_class == "Shadowblade":
            dmg = random.randint(110, 160)
        elif player_class == "Scholar":
            dmg = random.randint(125, 150)
        elif player_class == "Guardian":
            dmg = random.randint(120, 150)
        else:
            dmg = 50 # Default fallback if class not found

    print(f"\n--- Parsed Result ---")
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
