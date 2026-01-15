
from pathlib import Path
from utils import load_file

PROMPTS_DIR = Path(__file__).parent / "prompt"
# print(Path(__file__).parent)
# print('*'*50)
# print(PROMPTS_DIR)
# print('*'*50)
def load_prompt(file_path: str) -> str:
    """
    Loads the prompt template from a file.
    :param file_path: The path to the prompt template file.
    :type file_path: str
    :return: The content of the prompt template file as a string.
    :rtype: str
    """
    
    return load_file(PROMPTS_DIR / file_path)


PROMPT = load_prompt("react.md")
# print(PROMPT)

def generate_prompt(user_input: str) -> str:
    """
    Generates a prompt using the given strategy : Default: react.
    :type user_input: str
    :return: The constructed prompt string.
    :rtype: str
    """
    template = PROMPT
    return f"{template} \n\n User Message : {user_input.strip()} \nStep-by-step Reasoning:"