from handlers.base_handler import CommandHandler
from services.message_service import send_message
from services.database_service import Database
from config.env_config import *


class BuyerHandler(CommandHandler):
    def handle(self, message):
        super().handle(message)
        if message['text'].upper() == "ME":
            send_message(message['chat']['id'], "You are recognized as a Buyer.")
        elif "|" in message['text']:
            commands = message['text'].split("|")
            user_id = message['chat']['id']
            if len(commands) > 2 and commands[0] == "/new":
                title = commands[1]
                text = commands[2]
                self.new_note(user_id, title, text)
            elif len(commands) > 1 and commands[0] == "/delete":
                title = commands[1]
                self.delete_note(user_id, title)

    def new_note(self, user_id, title, text):
        db = Database()
        db.add_note_from_buyer(user_id, title, text)
        send_message(ADMIN_ID, f"User {user_id} add note {title} : {text}")

    def delete_note(self, user_id, title):
        db = Database()
        db.delete_note_from_buyer(user_id, title)
        send_message(ADMIN_ID, f"User {user_id} delete note {title} from db")
