
import os
from dotenv import load_dotenv
from pathlib import Path


PROJECT_ROOT = Path(__file__).parent  #D:\GenAI_CodingNinjas\Day-10\ScamGuardAI\scam-guard_ai   
load_dotenv(PROJECT_ROOT/".env")  # Load environment variables from .env file

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")    

DEFAULT_MODEL =  "gemini-2.5-flash-lite"
MAX_RETRIES = 3
RETRY_DELAY = 2

#paths
OUTPUT_DIRECTORY = PROJECT_ROOT / "outputs"
LOG_DIRECTORY = PROJECT_ROOT / "logs"

# Ensure output and log directories exist
OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True) 
LOG_DIRECTORY.mkdir(parents=True, exist_ok=True)    
# parents=True creates any necessary parent directories as well. 
# exist_ok=True prevents an error if the directory already exists.
# In combination: parents=True, exist_ok=True, Creates the full nested path if needed.
# Does not error if: # Some or all of the directories already exist.