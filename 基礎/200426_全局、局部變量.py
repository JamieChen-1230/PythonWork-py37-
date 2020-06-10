# name = "Jamie"  # 全局變量(未縮進)
# def subroutine_1():
#     x = 1  # 局部變量(有縮進)
#     # 當子程序內找不到匹配的局部變量時，會向外層作用域中查找
#     print(name)  # => Jamie，子程序也能調用全局變量
#     return x
# print(subroutine_1())  # => 1


# name = "Jamie"  # 全局變量
# def subroutine_2():
#     name = "SB"  # 局部變量，跟外面的全局變量毫無關係
#     # 優先查找子程序內匹配的局部變量
#     print(name)  # => SB 若全局變數和局部變數名稱相同時，優先使用"局部變量"
# print(subroutine_2())  # => None，因為沒有回傳值
# print(name)  # => Jamie，沒有聲明global的局部變量不會影響到全局變量


# name = "Jamie"  # 全局變量
# def subroutine_3():
#     global name  # 把name設為全局變量
#     name = "SB"  # 全局變量，並重新賦值給全局變量
#     print(name)  # => SB
# subroutine_3()
# print(name)  # => SB 因在子程序內已被改變


# name = ["Jamie", "sb"]  # 全局變量
# def subroutine_4():
#     # 無法更改變量本身，但如果是可變類型，可以對其內部元素做改變
#     name.append("nb")  # 可以進行內部元素操作
#     print(name)  # => ['Jamie', 'sb', 'nb']
# subroutine_4()
# print(name)  # => ['Jamie', 'sb', 'nb']


# def a():
#     name = "a"
#     print(name, end=" ")  # a
#     def b():
#         name = "b"
#         print(name, end=" ")  # b
#         def c():
#             name = "c"
#             print(name, end=" ")  # c
#         print(name, end=" ")  # b
#         c()
#     b()
#     print(name, end=" ")  # a
# a()  # => a b b c a


# name = "jamie"
# def a():
#     name = "sb"
#     def b():
#         global name  # 全局變量(name = "jamie")
#         name = "87"
#     b()
#     # 函數a中沒有把name設成全局變量，所以不會被影響
#     print(name)  # => sb，因優先讀取局部變量
# print(name)  # => jamie
# a()
# print(name)  # => 87 因在b()中更改了全局變量


# name = "jamie"
# def a():
#     name = "sb"
#     def b():
#         # name = "87"
#         def c():
#             # 用來在函式或其他作用域中使用外層(非全域性)變數
#             # 若b()沒有，則去找a()，一層一層往上找，找到後就停止，並把nonlocal變量指向他
#             # 若所有外層(a(),b()，不包括全域變數)都沒有相同名稱變量，則會報錯
#             nonlocal name
#             name = 'NB'
#         c()
#     b()
#     print(name)  # => NB，因在b()中更改了上一級變量
# print(name)  # => jamie
# a()
# print(name)  # => jamie，函數內沒使用global去改動


# # ※重要： 調用函數()只是代表指向他，不代表是真的複製一份到這邊運行
# name = "jamie"
# def a(func):
#     name = "sb"
#     func()
# def b():
#     print(name)  # => jamie，func()只是指向b()的函數體，不代表是在a()中運行
# a(b)


"""
總結：
    一、global關鍵字： 用來在函式或其他作用域中使用全域性變數。
        - 全域性變數：在最外層所設的變量
    二、nonlocal關鍵字： 用來在函式或其他作用域中使用外層(非全域性)變數。
        - 使用nonlocal關鍵字，他會一層一層的向外匹配到相同變量名的變量，並在內存中指向它
        - 若所有外層中(不包括全域變數)都沒有相同名稱變量，則會報錯
    三、調用函數()只是代表指向並調用它，不代表是真的複製一份到這邊(調用的地方)運行。
    四、如果函數內無global關鍵字：
                  - 有聲明局部變量： 讀取局部變量，且無法對全局變量重新賦值
                  - 無聲明局部變量： 讀取全局變量，且無法對全局變量重新賦值，但可以進行內部元素操作
            如果函數內有global關鍵字：
                  - 有聲明局部變量： 此局部變量被當作全局變量操作
                  - 無聲明局部變量： 讀取全局變量，且可以對全局變量重新賦值，也可以進行內部元素操作
            格式： 全局盡量變量用大寫，局部變量小寫，方便以後程式瀏覽。
"""
