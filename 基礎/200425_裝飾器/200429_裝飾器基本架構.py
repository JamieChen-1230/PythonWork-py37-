"""
裝飾器結構  = 高階函數 + 函數嵌套 + 閉包
"""

# ------裝飾器的基本架構(1)------
# import time
#
#
# def timmer(func):  # func = foo
#     def wrapper():
#         # print(func)
#         start = time.time()
#         func()  # 運行foo()
#         end = time.time()
#         print("運行時間%s" % (end - start))
#     return wrapper
#
#
# @timmer   # @timmer 相當於 foo = timmer(foo)，此時foo為wrapper的別名
# def foo():  # 符合不修改被修飾函數的原代碼
#     time.sleep(1)
#     print("running foo.")
#
#
# foo()  # 實際意義上等於執行wrapper()，符合不修改被修飾函數的調用方法


# ------裝飾器的基本架構+返回值(2)------
# import time
#
#
# def timmer(func):  # func = foo
#     def wrapper():
#         start = time.time()
#         res = func()  # 運行foo()
#         end = time.time()
#         print("運行時間%s" % (end - start))
#         return res  # 因為實際上是執行wrapper()，所以要有返回值要從這return
#     return wrapper
#
#
# @timmer   # @timmer 相當於 foo = timmer(foo)
# def foo():
#     time.sleep(1)
#     print("running foo.")
#     return "foo的返回值"
#
#
# res = foo()  # 執行wrapper()
# print(res)  # => foo的返回值，實際上是從wrapper()回傳過來的


# ------裝飾器的基本架構+返回值+參數(3) = 裝飾器------
import time


def timmer(func):
    # 不能把參數寫死，因為每個函數參數不同
    # def wrapper(name, age):
    #     start = time.time()
    #     res = func(name, age)
    #     end = time.time()
    #     print("運行時間%s" % (end - start))
    #     return res
    def wrapper(*args, **kwargs):  # 不能把參數寫死，因為每個函數參數不同
        print(args, *args)
        start = time.time()
        # args = ('jamie', 18, "man"), kwargs = {}，
        # 必須要加*號，不然就會傳成元組和字典過去，導致參數對應不上
        res = func(*args, **kwargs)
        end = time.time()
        print("運行時間%s" % (end - start))
        return res  # 因為實際上是執行wrapper()，所以要有返回值要從這return
    return wrapper


@timmer   # @timmer 相當於 foo = timmer(foo)
def foo(name, age):
    time.sleep(1)
    print(name, age)  # => jamie 18
    return "foo的返回值"


res = foo('jamie', 18)  # 執行wrapper()
print(res + "\n")  # => foo的返回值，實際上是從wrapper()回傳過來的


@timmer
def foo_2(name, age, gender):
    time.sleep(1)
    print(name, age, gender)  # => jamie 18 man
    return "foo_2的返回值"


res = foo_2('jamie', 18, "man")  # 執行wrapper()
print(res + "\n")  # => foo_2的返回值，實際上是從wrapper()回傳過來的


@timmer
def foo_3(name_list):
    time.sleep(1)
    for name in name_list:
        print(name)
    return "foo_3的返回值"


res = foo_3(["jamie", "annie"])
print(res + "\n")
