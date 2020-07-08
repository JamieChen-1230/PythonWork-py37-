# ------使用裝飾器模仿認證功能(有參數)------
# 當前用戶信息
current = {'username': None, 'login': False}  # 要用來記錄帳戶是否登陸，這樣才不用每刷新頁面都要重登
# 用戶清單
user_list = [
    {'name': "jamie", 'passwd': "123"},
    {'name': "sb", 'passwd': "123"},
    {'name': "nb", 'passwd': "123"}
]


def auth(auth_type="local"):
    def auth_func(func):
        def wrapper(*args, **kwargs):
            if auth_type == "local":
                print("目前資料讀取自 %s" % auth_type)
                if current["username"] and current["login"]:  # 已登入就直接進入頁面
                    print("用戶【%s】已登入" % current["username"])
                    res = func(*args, **kwargs)  # 認證後可繼續執行功能
                    return res
                username = input("帳號 ").strip()
                password = input("密碼 ").strip()
                for user in user_list:  # for_else
                    if username == user["name"] and password == user["passwd"]:
                        res = func(*args, **kwargs)
                        current["username"] = username  # 第一次登陸成功後保持都登入狀態
                        current["login"] = True
                        return res
                else:
                    print("帳號或密碼錯誤")
            elif auth_type == "sql":
                print("目前資料讀取自 %s" % auth_type)
        return wrapper
    return auth_func


# 這邊做了兩步驟：
# (1) @auth() ---> auth_func = auth(auth_type = "local")
# (2) @auth_func(且附加了auth_type) ---> index = auth_func(index)
# 相當於執行了：index = auth(auth_type="local")(index)
@auth()
def index():
    print("歡迎來到主頁")


@auth(auth_type="sql")
def home(name):
    print("%s~歡迎回家" % name)


@auth(auth_type="local")
def shopping_car(name):
    print("%s目前已選購 [%s, %s, %s]" % (name, "奶茶", "妹妹", "娃娃"))


index()
home("jamie")
shopping_car("jamie")


"""
結論：
    一、裝飾器(無參數)的基本架構為【高階函數+函數嵌套+閉包】。
    二、有參數化的裝飾器至少會有兩層嵌套。
        deco_2 = deco_1(裝飾器之參數設定)
        test = deco_2(test)
"""
