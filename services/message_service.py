import requests
import json
from config.env_config import *


def send_message(chat_id, text):
    url = API_URL + "sendMessage"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)
