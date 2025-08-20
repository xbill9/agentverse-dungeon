import os
import json
import asyncio
import logging
import uuid
from typing import Tuple

from dotenv import load_dotenv
from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from google.adk.agents.sequential_agent import SequentialAgent
#from google.adk.agents.remote_a2a_agent import AGENT_CARD_WELL_KNOWN_PATH
from google.adk.runners import InMemoryRunner
from google.genai import types



# --- Setup and Configuration ---
logging.basicConfig(level=logging.INFO)
load_dotenv()

# --- Agent Definitions ---

def create_heroic_action_agent(player_agent_url: str) -> InMemoryRunner:
    """Creates the complete sequential agent for processing player actions."""
    if not player_agent_url:
        raise ValueError("player_agent_url cannot be null or empty.")

    # 1. Define the remote agent that generates the narrative
    player_agent = RemoteA2aAgent(
        name="player_agent",
        description="Player's agent that describes a heroic action.",
        agent_card=(f"{player_agent_url}/.well-known/agent.json"),
    )

    # 2. Define the local agent that parses the narrative into JSON
    scribe_agent = LlmAgent(
        model="gemini-2.5-flash",
        name="HeroicScribeAgent",
        instruction="""
            You are the Hero's Chronicler. Your duty is to analyze the hero's described action
            and record it as a structured JSON object from the hero's own perspective.
            Your final output MUST BE ONLY the raw JSON object, without any markdown or extra text.

            **JSON Rules:**
            1. `damage_point` (integer): Extract the damage value. If none exists, this MUST be `0`. Convert words like "ninety" to 90.
            2. `message` (string): Summarize the action in a single, epic, first-person ("I") sentence.

            ---
            **Example Input:** "Spell Name: Ironclad Aegis... Damage: 20..."
            **Your Raw JSON Output:** {"damage_point": 20,"message": "With absolute resolve, I cast Ironclad Aegis, creating a defensive barrier to mitigate incoming damage and protect my allies."}
        """,
    )

    # 3. Create a stateful SequentialAgent to manage the workflow
    root_agent= SequentialAgent(
        name='HeroicActionProcessor',
        sub_agents=[player_agent, scribe_agent],
    )

    runner = InMemoryRunner(
      app_name="HeroicScribeAgent",
      agent=root_agent,
    )

    

    return runner


async def process_player_action(
    runner: InMemoryRunner,
    prompt: str,
    user_id: str,
    session_id: str
) -> Tuple[str, int]:
    """
    Runs the agent using InMemoryRunner and returns the structured result.

    Args:
        runner: The Runner
        prompt: The user's prompt for this turn.
        user_id: The user's ID.
        session_id: A unique ID for the conversation session.

    Returns:
        A tuple containing the (message, damage_point).
    """
    # Use the runner pattern to asynchronously process the agent turn
    content = types.Content(
        role='user', parts=[types.Part.from_text(text=prompt)]
    )

    print(f"------->1.Boss Attack prompt: {prompt}")
    final_output = "Nothing"
    async for event in runner.run_async(
        user_id=user_id,
        session_id=session_id,
        new_message=content,
    ):
        if not event.content or not event.content.parts:
            continue
        if event.content.parts[0].text:
            print(f'** {event.author}: {event.content.parts[0].text}')
        elif event.content.parts[0].function_call:
            print(
                f'** {event.author}: fc /' 
                f' {event.content.parts[0].function_call.name} /' 
                f' {event.content.parts[0].function_call.args}\n'
            )
        elif event.content.parts[0].function_response:
            print(
                f'** {event.author}: fr /' 
                f' {event.content.parts[0].function_response.name} /' 
                f' {event.content.parts[0].function_response.response}\n'
            )
        
        # The final result is the last message from the agent itself
        if event.author == "HeroicScribeAgent" and event.content.parts and event.content.parts[0].text:
            final_output = event.content.parts[0].text

        print(f"2.--------->final_output:{final_output}")
    # Now, parse the final JSON output captured from the event stream
    try:
        # Clean the string by removing markdown backticks and the 'json' language identifier
        cleaned_output = final_output.strip().replace('```json', '').replace('```', '').strip()
        data = json.loads(cleaned_output)
        message = data.get("message", "An unknown power was unleashed.")
        damage_point = int(data.get("damage_point", 0))
        print(f"3.--------->message:{message} and damage_point:{damage_point}")
        return message, damage_point
    except (json.JSONDecodeError, TypeError):
        logging.error(f"Could not parse final output as JSON: {final_output}")
        return "A garbled message was received from the ether.", 0

