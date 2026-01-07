
from pathlib import Path
import logging
import re
import json

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