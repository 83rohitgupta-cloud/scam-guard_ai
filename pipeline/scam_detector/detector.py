# imports
from typing import Any, Dict, List
from .executor import LLMExecutor
from .parser import OutputParser
from .builder import build_prompt
from utils import get_logger

logger = get_logger(__name__)

class ScamDetector:
    """
    A class to detect whether a given message is a scam or not.
    """

    def __init__(self, strategy: str = "react") -> None:
        """
        Initializes the ScamDetector instance.
       
        """
        logger.info("ScamDetector instance created.")
        self.executor = LLMExecutor
        self.parser = OutputParser
        self.strategy = strategy
        logger.info("Initialized the ScamDetector with strategy: %s", self.strategy)

    def detect(self, message: str) -> Dict[str, Any]:
        """
        Detects whether the given message is a scam or not.
        :param self : Description
        :param strategy: The detection strategy to use. Default is "react".
        :type strategy: str
        """
        logger.info("Starting scam detection for the message.")
        try:
            prompt =  build_prompt(message, self.strategy) 
            raw_response = self.executor.execute(prompt)
            parsed_result = self.parser.parse(raw_response)
            logger.info("Scam detection completed successfully.")
            return parsed_result

        except Exception as e:
            logger.error("Error during scam detection: %s", e)
            raise e
        
