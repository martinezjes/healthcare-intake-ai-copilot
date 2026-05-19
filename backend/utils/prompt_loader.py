from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

PROMPTS_DIR = PROJECT_ROOT / "prompts"


def load_prompt(filename: str) -> str:

    prompt_path = PROMPTS_DIR / filename

    with open(prompt_path, "r", encoding="utf-8") as file:
        return file.read()