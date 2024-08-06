from DB import db_handle
import time

def check_money(login_user):
    user_data = db_handle.get_data(login_user)
    return user_data["money"]

now_time = time.strftime("%x %X")

def recharge(login_user,money):
    user_data = db_handle.get_data(login_user)
    user_data["money"] += money
    acc_info = rf"{now_time}存款{money}元,当前余额是{user_data['money']}元"
    user_data["account"].append(acc_info)
    db_handle.save_data(user_data)
    return True,acc_info
def take_money(login_user,money):
    user_data = db_handle.get_data(login_user)
    if user_data["money"] > money:
        user_data["money"] -= money
        acc_info = rf"{now_time}取款{money}元,当前余额是{user_data['money']}元"
        user_data["account"].append(acc_info)
        db_handle.save_data(user_data)
        return True,acc_info
    else:
        return False,"取款失败,余额不足"

def get_acc(login_user):
    user_data = db_handle.get_data(login_user)
    return user_data["account"]