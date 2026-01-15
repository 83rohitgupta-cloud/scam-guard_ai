
from typing import Any
from utils import get_logger, extract_json_from_text
logger = get_logger(__name__)


class OutputParser:
    """
    A class to parse the output from the LLM response.
    """

    def parse_llm_output(self, llm_output: str) -> dict[str, Any]:
        """
        Extract and Parse JSON structure from the LLM output.

        Args:
            llm_output: Raw text output from LLM
        
        Returns:
            Dictionary that contains results from the LLM output
            - label: str -> Classification result (Scam | No Scam | Uncertain), 
            - reasoning: str -> Analysis of the classification,
            - intent: str -> Description of the user's intent,
            - risk_factors: List[str] -> List of identified red flags
        """
        logger.info("Parsing LLM response.")
        try:
            parsed_output = extract_json_from_text(llm_output)
            logger.info("LLM response parsed successfully.")
            return parsed_output
        except Exception as e:
            logger.error("Error parsing LLM response: %s", e)
            fall_back_output = {
                "label": "Uncertain", 
                "reasoning": "Could not parse AI response",
                "intent": "Unknown",
                "risk_factors": ["Parsing Error"]
            }
            return fall_back_output
    