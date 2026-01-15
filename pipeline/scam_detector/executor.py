
from typing import Optional
from llm.client import LLMClient
from utils import get_logger

logger = get_logger(__name__)

class LLMExecutor:
    """
    A class to execute LLM prompts and return responses.
    """
    def __init__(self, model: Optional[str] = None) -> None:
        """
        Initializes the LLMExecutor instance.
        :param model: The language model to use. Default is None.
        :type model: Optional[str]
        """
        self.llm: LLMClient = LLMClient(model) if model else LLMClient()

        logger.info("LLMExecutor initialized with model: %s", model)

   
    def execute(self, prompt: str) -> str:
        """
        Executes the prompt using LLM client and returns raw response.

        Args:
            prompt: The formatted prompt string to send to LLM.
        Returns:
            Raw response from LLM.
        Raises:
            Exception: When LLM call fails.
        """
        logger.info(f"Executing LLM with final prompt")
        try:
            response = self.llm.call(prompt)
            logger.info("LLM execution is successful!")

            return response
        
        except Exception as e:
            logger.error(f"LLM execution failed: {str(e)}")
            raise
            