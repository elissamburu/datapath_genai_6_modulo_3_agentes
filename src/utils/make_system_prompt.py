from src.prompts.templates import SYSTEM_DEFAULT_PROMPT

def make_system_prompt(suffix: str) -> str:
    return SYSTEM_DEFAULT_PROMPT.format(suffix=suffix)
