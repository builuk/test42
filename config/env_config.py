from dotenv import dotenv_values
import os

config = dotenv_values("../.env")
TOKEN = config.get('TOKEN')
ADMIN_ID = config.get('ADMIN_ID')
API_URL = f"https://api.telegram.org/bot{TOKEN}/"
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config'))