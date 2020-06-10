# ------------------- 動態導入模塊 -------------------
# import importlib
# # 直接返回需要的模塊
# m = importlib.import_module("module.t")
# print(m)  # => <module 'module.t' from 'D:\\PythonWork\\SelfLearn\\基礎\\180727_動態導入模塊\\module\\t.py'>
# m.foo1()  # => test1
# m._foo2()  # => test2


# # _方法名在使用import *時會被略過，所以不能調用
# from module.t import *
#
# foo1()  # => test1
# # _foo2()  # => error，_變量
#
# from module.t import foo1,_foo2
#
# foo1()  # => test1
# _foo2()  # => test2，這只是種約定還是可以被調用，只有import*時會被隱藏


