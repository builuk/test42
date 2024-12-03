import requests
from datetime import datetime, timedelta
from handlers.base_handler import CommandHandler
from services.message_service import send_message
from services.user_service import check_user_role
from services.database_service import Database
from config.env_config import *
from helper.handler_helper import CommandHandlerFactory


# Оновлення check_user_role для використання бази даних
def check_user_db_role(user_id):
    if user_id == ADMIN_ID:
        return 'admin'
    db = Database()
    role_data = db.get_user_roles(user_id)
    role = extract_unique_word(role_data)
    if role:
        return role
    else:
        # За замовчуванням додаємо роль "guest"
        db.add_user_role(user_id, "guest")
        return "guest"


def extract_unique_word(data):
    # Розгортаємо вкладені кортежі в список рядків
    words = [item[0] for item in data if item]  # Перевіряємо, що кортеж не порожній
    # Повертаємо унікальне слово, якщо всі слова однакові
    return words[0] if len(set(words)) == 1 else None


def main_loop(duration_minutes=5):
    db = Database()
    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=duration_minutes)
    offset = 0

    print(f"Bot started. Running for {duration_minutes} minutes...")
    while datetime.now() < end_time:
        response = requests.get(API_URL + f"getUpdates?offset={offset}")
        updates = response.json().get('result', [])
        for update in updates:
            offset = update['update_id'] + 1
            message = update.get('message')
            if message and 'text' in message:
                user_id = str(message['from']['id'])
                role = check_user_db_role(user_id)
                handler = CommandHandlerFactory().get_handler(role)
                handler.handle(message)
        # Виводимо залишок часу кожну хвилину
        print(f"Time remaining: {(end_time - datetime.now()).seconds // 60} minutes")

    print("Bot finished running.")


if __name__ == "__main__":
    main_loop()
