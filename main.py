#imports
from pathlib import Path
import sys
from pipeline.sam_detector.detector import ScamDetector
from utils import get_logger

#path normalization
project_root = Path(__file__).parent    #D:\GenAI_CodingNinjas\Day-10\ScamGuardAI\scam-guard_ai
sys.path.append(str(project_root))

"""
 sys.path is a list of strings that specifies the directories where Python looks for modules when you use statements like import. The sys.path.append method allows you to dynamically add new directories to this list during the execution of a Python script.
 This is useful when you are working on a project with a complex directory structure.
"""
logger = get_logger(__name__)   #In Python, __name__ contains the full name of the current module,  practice of using __name__, which accurately reflects the module hierarchy in logging names.

#main function
def main():
    """
    Main function that run the scam detection workflow.
    """
    detector = ScamDetector()

    test_message = "Congratulations! You've won a free cruise to the Bahamas. Click here to claim your prize."
    try:
        logger.info(f" Running the scam detection workflow")
        result = detector.detect(test_message)
        print(f"Input message from the user : {test_message}")
        print(f"Detetcion result : {result}")
        logger.info(f"Completed the scam detection workflow Successfully.")
    except Exception as e:
        logger.error(f"Error during scam detection : {e}")
        print(f"Error during scam detection : {e}")

#calls thescam detection workflow - class

if __name__ == "__main__":
    main()