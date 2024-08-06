from core import src

def is_login(f):
    def check(*args,**kwargs):
        if src.login_user:
            res = f(*args,**kwargs)
            return res
        else:
            print("你还没登录,请先登录")
            src.login()
    return check