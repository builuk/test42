import requests
import json
from handlers.base_handler import CommandHandler
from services.message_service import send_message
from services.user_service import check_user_role
from config.env_config import *
from helper.handler_helper import CommandHandlerFactory
import requests
import requests
import json

class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.api_url = f"https://api.telegram.org/bot{token}/"

    def get_updates(self, offset=None):
        url = self.api_url + "getUpdates?timeout=100"
        if offset:
            url += f"&offset={offset}"
        response = requests.get(url)
        return json.loads(response.content)

    def send_message(self, chat_id, text, reply_markup=None):
        if not text:  # Перевірка, чи є текст у повідомленні
            print("Error: Message text is empty. Skipping sending.")
            return
        url = self.api_url + "sendMessage"
        headers = {'Content-Type': 'application/json'}
        data = {
            "chat_id": chat_id,
            "text": text
        }
        if reply_markup:
            data['reply_markup'] = reply_markup

        response = requests.post(url, headers=headers, json=data)
        print(f"Message sent to {chat_id}, server response: {response.text}")

    def create_start_keyboard(self):
        keyboard = [
            [{"text": "Додати роль", "callback_data": "add_role"}],
            [{"text": "Видалити роль", "callback_data": "delete_role"}]
        ]
        return {"inline_keyboard": keyboard}

    def handle_updates(self, updates):
        for update in updates.get('result', []):
            if 'message' in update:
                self.handle_message(update['message'])
            elif 'callback_query' in update:
                self.handle_callback(update['callback_query'])

    def handle_message(self, message):
        chat_id = message['chat']['id']
        text = message.get('text', '').strip().lower()

        if text == "/start":
            reply_markup = self.create_start_keyboard()
            self.send_message(chat_id, "Ласкаво просимо! Оберіть опцію:", reply_markup)
        elif text == "/echo":
            echo_text = message['text'][6:] if len(message['text']) > 6 else "Нічого повторювати."
            self.send_message(chat_id, echo_text)
        else:
            self.send_message(chat_id, "Команда не розпізнана.")

    def handle_callback(self, callback_query):
        chat_id = callback_query['message']['chat']['id']
        data = callback_query['data']

        if data == "add_role":
            self.send_message(chat_id, "Введіть ID користувача, щоб додати роль:")
        elif data == "delete_role":
            self.send_message(chat_id, "Введіть ID користувача, щоб видалити роль:")

if __name__ == "__main__":
    bot = TelegramBot(TOKEN)

    last_update_id = None
    while True:
        updates = bot.get_updates(last_update_id)
        if updates.get("result"):
            last_update_id = updates["result"][-1]["update_id"] + 1
            bot.handle_updates(updates)
