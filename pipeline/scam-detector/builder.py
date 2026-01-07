"""
This file contains main prompt generation functionality.
Module to build prompts for the scam detection model. With the "react" strategy, it generates a prompt that encourages the model to reason step-by-step before arriving at a conclusion.
"""

from llm.prompts.prompts import generate_prompt

def build_prompt(message: str, strategy: str) -> str:
    """
    Builds the prompt for the scam detection model based on the given message and strategy.
    :param message: The input message to be evaluated.
    :type message: str
    :param strategy: The detection strategy to use.
    :type strategy: str
    :return: The constructed prompt string ready for LLM consumption.
    :rtype: str
    """
    if strategy == "react":
        return generate_prompt(message)
    else:
       raise NotImplementedError(f"Strategy {strategy} is not implemented.")



