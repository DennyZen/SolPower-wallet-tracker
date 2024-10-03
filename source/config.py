
from dotenv import load_dotenv
import os
from loguru import logger
logger.add("log.log", rotation="7 day", compression="zip", level="TRACE", backtrace=True, diagnose=True)

load_dotenv()

MONGODB_URI = os.getenv('MONGODB_URI', '')
BOT_TOKEN = os.getenv('BOT_TOKEN', '')
HELIUS_KEY = os.getenv('HELIUS_KEY', '')
HELIUS_WEBHOOK_URL = os.getenv('HELIUS_WEBHOOK_URL', '')
HELIUS_WEBHOOK_ID = os.getenv('HELIUS_WEBHOOK_ID', '')

logger.debug(f'MONGODB_URI: {MONGODB_URI}')
logger.debug(f'BOT_TOKEN: {BOT_TOKEN}')
logger.debug(f'HELIUS_KEY: {HELIUS_KEY}')
logger.debug(f'HELIUS_WEBHOOK_URL: {HELIUS_WEBHOOK_URL}')
logger.debug(f'HELIUS_WEBHOOK_ID: {HELIUS_WEBHOOK_ID}')