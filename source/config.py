
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URI = os.getenv('MONGODB_URI', '')
BOT_TOKEN = os.getenv('BOT_TOKEN', '')
HELIUS_KEY = os.getenv('HELIUS_KEY', '')
HELIUS_WEBHOOK_URL = os.getenv('HELIUS_WEBHOOK_URL', '')
HELIUS_WEBHOOK_ID = os.getenv('HELIUS_WEBHOOK_ID', '')