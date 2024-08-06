from DB import db_handle
def register_info(user_name,password):
    user_info = {
        "user_name": user_name,
        "password": password,
        "money": 200,
        "account": []
    }
    user_date = db_handle.get_data(user_name)
    if user_date:
        return False,"注册失败,用户已存在,不能重新注册"
    db_handle.save_data(user_info)
    return True,f"{user_name}注册成功"

def login_info(user_name,password):
    user_data = db_handle.get_data(user_name)
    if user_data:
        if password == user_data["password"]:
            return True,f"{user_name}登录成功"
        return False,"密码错误"
    return False,"用户名不存在,请重新登录"










