
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