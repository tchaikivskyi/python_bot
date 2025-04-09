from rich.prompt import Prompt
from rich.console import Console

__console__ = Console()

def colored_input(prompt_text: str, color: str = "green") -> str:
    formatted_prompt = f"[{color}]{prompt_text}[/]"
    return Prompt.ask(formatted_prompt)

def colored_text(text: str, color: str = "green") -> None:
    formatted_text = f"[{color}]{text}[/]"
    __console__.print(formatted_text)