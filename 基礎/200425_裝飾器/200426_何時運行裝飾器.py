"""
裝飾器特性：
    一、能把被裝飾的函數替換成另一個函數。(參考 200425_基礎知識)
    二、裝飾器在被裝飾函數定義時就會執行，這通常是發生在加載模塊時。
"""

registry = []


def deco(func):
    print("running deco. ------> 模塊加載時就會運行")

    def inner():
        print("running %s. ------> 調用%s時運行" % (func, func.__name__))
        func()
        registry.append(func)
    return inner


@deco  # @deco 相當於執行了 f1 = deco(f1)
def f1():
    print("running f1.")


@deco  # @deco 相當於執行了 f2 = deco(f2)
def f2():
    print("running f2.")


f1()  # 運行的是裝飾器下的inner函數
f2()  # 運行的是裝飾器下的inner函數
print("registry -> %s" % registry)
