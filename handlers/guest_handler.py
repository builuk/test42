from handlers.base_handler import CommandHandler
from services.message_service import send_message
from config.env_config import *


class GuestHandler(CommandHandler):
    def handle(self, message):
        super().handle(message)
        if message['text'].upper() == "ME":
            send_message(message['chat']['id'], "Please register to use the bot functionalities.")