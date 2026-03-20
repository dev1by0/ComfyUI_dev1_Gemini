from .gemini_node import Dev1GeminiAdvanced
from .task_prompt_manager import Dev1TaskPromptManager, Dev1PromptCombiner
from .api_routes import *  # Import API routes

NODE_CLASS_MAPPINGS = {
    "Dev1GeminiNode": Dev1GeminiAdvanced,
    "Dev1TaskPromptManager": Dev1TaskPromptManager,
    "Dev1PromptCombiner": Dev1PromptCombiner
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Dev1GeminiNode": "Dev1 Gemini",
    "Dev1TaskPromptManager": "Dev1 Task Prompt Manager",
    "Dev1PromptCombiner": "Dev1 Prompt Combiner"
}

# Path to web directory relative to this file
WEB_DIRECTORY = "./web"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]