"""
LLM Client for Google Gemini API with retry logic and incremental backoff.
"""

import time
from google import genai
from utils import get_logger
from config import GEMNI_API_KEY, DEFAULT_MODEL, MAX_RETRIES, RETRY_DELAY

logger = get_logger(__name__)

class LLMClient:
    """
    A client to interact with a Language Model (LLM) API.
    """

    def __init__(self, model_name = DEFAULT_MODEL, max_retries = MAX_RETRIES, retry_delay = RETRY_DELAY) -> None:
        """
        Initializes the LLMClient instance.
        :param model: The language model to use. Default is "gpt-3.5-turbo".
        :type model: str
        """
        self.model_name = model_name
        self.max_retries = max_retries
        self.retry_delay = retry_delay  
        self.client = genai.Client(api_key=GEMNI_API_KEY)
        logger.info("LLMClient initialized with model: %s", self.model_name)

    def call(self, prompt: str, **kwargs) -> str:
        """
        Calls the LLM API with the given prompt and returns the response.
        :param prompt: The prompt to be sent to the LLM.
        :type prompt: str
        :return: The response from the LLM.
        :rtype: str
        """
        logger.info("Calling LLM API with prompt.")
        # Simulated LLM response for demonstration purposes.
        for attempt in range(1, self.max_retries + 1):
            try:
                response = self.client.models.generate_content(
                    contents=prompt, 
                    model=self.model_name,
                    **kwargs
                )
                logger.info("LLM API call successful.")
                if response and response.text:
                    return response.text.strip()
                else:
                    raise ValueError("Empty response from LLM API")
            except Exception as e:
                logger.error("Error calling LLM API on attempt %d: %s", attempt, e)
                if attempt < self.max_retries:
                    logger.info("Retrying in %d seconds...", self.retry_delay)
                    time.sleep(self.retry_delay * (2 ** (attempt - 1)))  # Exponential backoff
                else:
                    logger.error("Max retries reached. Raising exception.")
                    raise e
      