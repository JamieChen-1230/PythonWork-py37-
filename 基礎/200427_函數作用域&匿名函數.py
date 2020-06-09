# ---------------- 作用域 ----------------
# # ※ 函數運行方式 => 函數內存位置+()
#
#
# def foo():
#     print("in the test")
#     return foo_1  # 返回test_1內存位置
#
#
# def foo_1():
#     print("in the test_1")
#
#
# res = foo()  # => in the test，res獲取test_1函數位置
# res_1 = res()  # => in the test_1，res()=test_1()
# print(res_1)  # => None，test_1無return

# # 作用域
# name = "jamie"
#
#
# def a():
#     name = "aaa"
#
#     def b():
#         name = "bbb"
#
#         def c():
#             name = "ccc"
#             print(name)
#         return c
#     return b
#
#
# res = a()  # 運行a()，並獲取b()內存位置
# print(res)  # b()內存位置
# res_1 = res()  # 運行b()，並獲取c()內存位置
# print(res_1)  # c()內存位置
# res_1()  # => ccc，運行c()
# a()()()  # => ccc


# ---------------- 匿名函數 ----------------
# # 基本結構
# f = lambda x: x+1  # x為形參，return x+1
# print(f)  # => 匿名函數內存地址
# print(f(10))  # => 11

# # 對比
# def sbname(name):  # 一般函數
#     return name + "_sb"
# print(sbname("jamie"))  # => jamie_sb
#
# sbname_2 = lambda name: name+"_sb"  # 匿名函數，正常來說不應該定義sbname_2
# print(sbname_2("jamie"))  # => jamie_sb

# # 練習
# func = lambda *args: args
# print(func(1, 2, 3))  # => (1, 2, 3)
#
# func = lambda *args: print(args)
# print(func(1, 2, 3))  # => None
#
# func = lambda *args: print(*args)
# print(func(1, 2, 3))  # => None
