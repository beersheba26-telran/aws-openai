from dotenv import load_dotenv  
from os import getenv
from pathlib import Path
load_dotenv()
FASTEMBED_MODEL_NAME = getenv("FASTEMBED_MODEL_NAME", "BAAI/bge-small-en-v1.5")
DOCUMENTS_PATH = Path(getenv("DOCUMENTS_PATH", "travel_policy.txt"))