# ------使用裝飾器模仿認證功能(無參數)------
import time

# 當前用戶信息
current = {'username': None, 'login': False}  # 要用來記錄帳戶是否登陸，這樣才不用每刷新頁面都要重登
# 用戶清單
user_list = [
    {'name': "jamie", 'passwd': "123"},
    {'name': "sb", 'passwd': "123"},
    {'name': "nb", 'passwd': "123"}
]


def auth_func(func):
    def wrapper(*args, **kwargs):
        if current["username"] and current["login"]:  # 已登入就直接進入頁面
            print("用戶【%s】已登入" % current["username"])
            res = func(*args, **kwargs)  # 認證後可繼續執行功能
            return res
        username = input("帳號 ").strip()
        password = input("密碼 ").strip()
        for user in user_list:  # for_else循環
            if username == user["name"] and password == user["passwd"]:
                res = func(*args, **kwargs)
                current["username"] = username  # 第一次登陸成功後保持都登入狀態
                current["login"] = True
                return res
        else:
            print("帳號或密碼錯誤")
    return wrapper


@auth_func
def index():
    print("歡迎來到主頁")


@auth_func
def home(name):
    print("%s~歡迎回家" % name)


@auth_func
def shopping_car(name):
    print("%s目前已選購 [%s, %s, %s]" % (name, "奶茶", "妹妹", "娃娃"))


index()
time.sleep(1)
home("jamie")
time.sleep(1)
shopping_car("jamie")
