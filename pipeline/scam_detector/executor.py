
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

    @staticmethod
    def execute(self, prompt: str) -> str:
        """
        Executes the given prompt using a language model and returns the response.
        :param prompt: The prompt to be executed.
        :type prompt: str
        :return: The response from the language model.
        :rtype: str
        """
        logger.info("Executing LLM prompt.")
        # Simulated LLM response for demonstration purposes.
        try :
            response = self.llm.call(prompt)
            logger.info("LLM prompt executed successfully.")
            return response
        except Exception as e:
            logger.error("Error executing LLM prompt: %s", e)
            raise e
            