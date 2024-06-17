from dotenv import load_dotenv
import os


load_dotenv()

OUTLINE_API_URL = os.environ.get("OUTLINE_API_URL")
OUTLINE_CERT    = os.environ.get("OUTLINE_CERT")
