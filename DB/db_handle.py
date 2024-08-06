import json
import os

from config.setting import file_path
def save_data(user_info):
    name = user_info["user_name"]
    with open(rf"{file_path}\{name}.json","w",encoding="utf-8") as f:
        json.dump(user_info,f)

def get_data(user_name):
    user = rf"{file_path}\{user_name}.json"
    if os.path.exists(user):
        with open(user,"r",encoding="utf-8") as f:
            user_data = json.load(f)
            return user_data

