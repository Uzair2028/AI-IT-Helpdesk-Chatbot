import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("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")

MODEL_NAME = "llama-3.3-70b-versatile"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"