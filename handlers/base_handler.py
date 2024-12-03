from services.message_service import send_message
from services.user_service import check_user_role
from config.env_config import *

class CommandHandler:
    def handle(self, message):
        # Логіка для команди GIVE_MY_ID, що доступна всім користувачам
        if message['text'].upper() == "GIVE_MY_ID":
            user_id = message['from']['id']
            send_message(user_id, f"Your ID is {user_id}")
        elif message['text'].upper() == "ROLE":
            user_id = message['from']['id']
            role = check_user_role(user_id)
            send_message(user_id, f"Your user role is {role}")


