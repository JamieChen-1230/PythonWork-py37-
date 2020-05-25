"""
因為Python並不支援重載方法或函數，所以為了要做到分派函數有以下兩種方法：
        一、if...elif...else：此方法雖然也能達到目的，但不容易做擴展。
        二、@singledispatch 裝飾器：根據第一個參數做到單分派泛函數且易於擴展。

單分派泛函數：
        單分派：根據一個參數的類型，以不同方式執行相同的操作的行為。
        多分派：可根據多個參數的類型選擇專門的函數的行為。
        泛函數：多個函數綁在一起組合成一個泛函數。
"""


from functools import singledispatch


# @singledispatch標記處理object類型的基函數
@singledispatch
def age(obj, name):
    print('請傳入合法類型的參數！')


# 各個專門函數使用 @base_function.register(<<type>>) 裝飾
@age.register(int)
def _(n, name):
    print('{}已經{}歲了。'.format(name, n))


@age.register(str)
def _(text, name):
    print('{} is {} years old.'.format(name, text))


@age.register(list)
@age.register(tuple)
def _(seq, name):
    for age in seq:
        print('{} is {} years old.'.format(name, age))


age(23, "Jamie")  # int
age('twenty three', "Jamie")  # str
age(['23', '24'], "Jamie")  # list
age({"22", "23"}, "Jamie")  # set，沒有設定專門函數的類型將會調用基函數
