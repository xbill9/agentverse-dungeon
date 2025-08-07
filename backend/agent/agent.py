import logging
from dotenv import load_dotenv
from google.adk.agents.llm_agent import LlmAgent
from google.adk.models.lite_llm import LiteLlm
import os

load_dotenv()


root_agent = LlmAgent(
    model="",
    name="Guardian_combat_agent",
    instruction="""
    """
)


