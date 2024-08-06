from api import user_i
from api import bank_i
from lib.common import is_login

#注册
def register():
    while True:
        user_name = input("请输入用户名")
        password = input("请输入你的密码")
        re_password = input("请再次输入你的密码")
        if re_password == password:
            flag,msg = user_i.register_info(user_name,password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print("密码不一致,请重新注册")

#登录
login_user = None
def login():
    while True:
        user_name = input("请输入用户名")
        password = input("请输入密码")
        flag,msg = user_i.login_info(user_name,password)
        if flag:
            print(msg)
            global login_user
            login_user = user_name
            break
        else:
            print(msg)

#余额
@is_login
def check_money():
    money = bank_i.check_money(login_user)
    print(rf"{login_user}当前余额是{money}")

#存款
@is_login
def recharge():
    while True:
        money = float(input("请输入存款金额"))
        flag,msg = bank_i.recharge(login_user,money)
        if flag:
            print(msg)
            break
        else:
            print(msg)
#取款
@is_login
def get_money():
    while True:
        money = float(input("请输入取款金额"))
        flag,msg = bank_i.take_money(login_user,money)
        if flag:
            print(msg)
            break
        else:
            print(msg)
#账单
@is_login
def account():
    acc = bank_i.get_acc(login_user)
    if acc:
        for i in acc:
            print(i)
    else:
        print("目前还没有流水账")

def run():
    while True:
        fun_select ={
            0:["退出",exit],
            1:["注册",register],
            2:["登录",login],
            3:["余额",check_money],
            4:["存款",recharge],
            5:["取款",get_money],
            6:["账单",account],
        }
        for k in fun_select:
            print(k,fun_select[k][0])
        select = int(input("请输入操作数>>>"))
        if select in fun_select:
            fun_select[select][1]()
        else:
            print("输出错误")