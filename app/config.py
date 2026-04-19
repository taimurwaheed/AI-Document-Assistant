import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
CHROMA_PATH = os.getenv("CHROMA_PATH", "chroma_db")