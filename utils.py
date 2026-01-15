
from pathlib import Path
import logging
import re
import json

def load_file(file_path: str) -> str:
    """
    Loads the content of a file and returns it as a string.
    :param file_path: The path to the file to be loaded.
    :type file_path: str
    :return: The content of the file as a string.
    :rtype: str
    """
    return Path(file_path).read_text(encoding='utf-8').strip()

def get_logger(name: str) -> logging.Logger:
    """
    Sets up and returns a logger with the specified name.
    log message to the console with specified format and level.
    log format: [timestamp] log level :  message
    log message levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
    """
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s : %(message)s"
        
    )

    return logging.getLogger(name)

def extract_json(text):
    """
    Finds the first '{' and the last '}' in a string 
    and parses it as JSON.
    """
    try:
        # Regex to find the JSON block inside the text
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
    except Exception as e:
        print(f"JSON Parsing Error: {e}")
    
    # Fallback if parsing fails
    return {
        "label": "Uncertain", 
        "reasoning": "Could not parse AI response",
        "intent": "Unknown",
        "risk_factors": ["Parsing Error"]
    }

def extract_json_from_text(text: str) -> dict:
    """Extract JSON from text string. Returns empty dict if not found."""
    try:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
        return {}
    except json.JSONDecodeError:
        return {}