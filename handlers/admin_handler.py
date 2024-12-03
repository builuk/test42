from handlers.base_handler import CommandHandler
from services.message_service import send_message
from services.database_service import Database
from config.env_config import *
import os


class AdminHandler(CommandHandler):
    def handle(self, message):
        super().handle(message)  # Виклик базового класу для загальної команди
        commands = message['text'].split("|")
        if len(commands) > 2 and commands[0] == "/role":
            user_id = commands[1]
            role = commands[2]
            self.set_role(user_id, role)
        elif len(commands) > 2 and commands[0] == "/delete_role":
            user_id = commands[1]
            role = commands[2]
            self.delete_role(user_id, role)
        elif len(commands) > 2 and commands[0] == "/db_role":
            user_id = commands[1]
            role = commands[2]
            self.set_db_role(user_id, role)
        elif len(commands) > 2 and commands[0] == "/db_new":
            user_id = commands[1]
            role = commands[2]
            self.set_db_role(user_id, role)
        elif len(commands) > 2 and commands[0] == "/db_delete_role":
            user_id = commands[1]
            role = commands[2]
            self.delete_db_role(user_id, role)

    def set_role(self, user_id, role):
        file_name = 'sellers.txt' if role == 'seller' else 'users.txt'
        file_path = os.path.join(BASE_DIR, file_name)
        if not os.path.exists(file_path):
            open(file_path, 'w').close()
        with open(file_path, 'a') as file:
            file.write(user_id + '\n')
        send_message(ADMIN_ID, f"User {user_id} set as {role}")

    def delete_role(self, user_id, role):
        file_name = 'sellers.txt' if role == 'seller' else 'users.txt'
        file_path = os.path.join(BASE_DIR, file_name)
        f = []
        with open(file_path, 'r') as file:
            f = file.readlines()
        f.remove(user_id + '\n')
        with open(file_path, 'w') as file:
            file.writelines(f)
        send_message(ADMIN_ID, f"User {user_id} delete as {role}")

    def set_db_role(self, user_id, role):
        db = Database()
        db.update_user_role(user_id, role)
        send_message(ADMIN_ID, f"User {user_id} set as {role} in db")

    def create_db_role(self, user_id, role):
        db = Database()
        db.add_user_role(user_id, role)
        send_message(ADMIN_ID, f"User {user_id} add as {role} in db")

    def delete_db_role(self, user_id, role):
        db = Database()
        db.delete_user_role(user_id, role)
        send_message(ADMIN_ID, f"User {user_id} delete as {role} in db")
