"""
裝飾器：是可調用的對象，其參數為另一個【函數】
        用途：一、裝飾器處理被裝飾之函數後，將原函數返回
                    二、裝飾器處理被裝飾之函數後，並返回另一個函數(大部分都是如此)
        原則：一、不修改被修飾函數的原代碼
                    二、不修改被修飾函數的調用方法
"""


# ---------返回原函數---------
def deco_1(func):
    print("running deco_1.")
    func()
    return func


@deco_1   # @deco_1 相當於執行了 target_1 = deco_1(target_1)
def target_1():
    print("running target_1.")


# ---------返回另一個函數---------
def deco_2(func):
    def wrapper():
        func()
        print("running deco_2.")
    return wrapper


@deco_2  # @deco_2 相當於執行了 target_2 = deco_2(target_2)
def target_2():
    print("running target_2.")


# 此時的target_2已經被裝飾器替換成wrapper函數了
print(target_2)  # => <function deco_2.<locals>.wrapper at 0x000001E7B92257B8>
target_2()  # 運行的是裝飾器下的wrapper函數
