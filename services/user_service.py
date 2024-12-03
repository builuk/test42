import os
from config.env_config import *


def check_user_role(user_id):
    if user_id == ADMIN_ID:
        return 'admin'
    user_id = str(user_id) + '\n'
    file_name = 'sellers.txt'
    file_path = os.path.join(BASE_DIR, file_name)
    f = open(file_path, 'rt')
    lines = f.readlines()
    f.close()
    if user_id in lines:
        return "seller"
    file_name = 'users.txt'
    file_path = os.path.join(BASE_DIR, file_name)
    f = open(file_path, 'rt')
    lines = f.readlines()
    f.close()
    if user_id in lines:
        return "buyer"
