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
        self.executor = LLMExecutor()
        self.parser = OutputParser()
        self.strategy = strategy
        logger.info("Initialized the ScamDetector with strategy: %s", self.strategy)

    def detect(self, message: str) -> Dict[str, Any]:
        """
        Runs the main scam detection pipeline.
        """
        logger.info(f"Started detection for input message")
        try:
            prompt = build_prompt(message, self.strategy)
            raw_response = self.executor.execute(prompt)
            parsed_result = self.parser.parse_llm_output(raw_response)
            
            logger.info(f"Detection successful!")
            return parsed_result

        except Exception as e:
            logger.error(f"Detection pipeline failed: {e}")        
