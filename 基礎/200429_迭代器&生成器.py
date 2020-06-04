# ------------------ 迭代器 ------------------
# 迭代器(Iterator)：
#   - 對象必須實現__next__()和__iter__()方法，執行此方法要嘛回傳下一項，要嘛回傳異常並終止迭代。(只能往下走不能往回走)
# 可迭代對象(Iterable)：
#   - 實現了__iter__()方法的對象，所以迭代器一定是可迭代對象
#   - 而其他包括str、list、dict等等都是可迭代對象，但他們不是迭代器，因為沒有__next__()方法
#   - 可使用for, sum, max等方法去訪問可迭代對象
# 使用for迴圈來遍歷比較好，因可以以統一的方式去實現可迭代對象和迭代器，且迭代器是只有當調用時才會存進內存(較省內存)

# ※ 本質上之前學的列表、元組、字典、字符串、集合與文件是可迭代對象，但都不屬於迭代器對象，只不過for循環會自動調用它們的__iter__()方法，讓它們變成了迭代器對象
# name = "SB"
# iter_name = name.__iter__()  # 變成了可迭代對象，可調用__next__()方法
# print(iter_name)  # => <str_iterator object at 0x000001AC62392FD0>
# print(iter_name.__next__())  # => S
# print(iter_name.__next__())  # => B
# print(iter_name.__next__())  # => 報錯(異常發生)

# 迭代器方法(能實現有序和無序數據類型，EX：字典(無序))
# li = [1, 2, 3]
# for i in li:  # 裡面自動調用 iter_li = li.__iter__(),  iter_li.__next__()
#     print(i)

# 不使用迭代器方法(只能實現有序數據類型)
# i = 0
# while i < len(li):
#     print(li[i])
#     i += 1

# 無序數據類型迭代
# dic = {'a': 1, "b": 2, "c": 3}
# iter_dic = dic.__iter__()  # iter_dic = 也可用iter(dic)
# print(iter_dic.__next__())  # => b，默認是keys
# print(iter_dic.__next__())  # => c
# print(next(iter_dic))  # => a，也可使用next()方法調用


# ------------------ 產生器(生成器)(generator) ------------------
# ※ 產生器是一種特別的迭代器對象，因為不用實作__iter__()和__next__()方法也能建立迭代器
#   - 語法上跟函數類似，差別在於使用yield返回值並保存當前狀態
#   - 自動實現迭代器協議

# ------生成器函數------
# def demo():
#     print("demo_in_1")
#     yield 1  # 也是回傳值，但不像return只能使用一次
#     print("demo_in_2")
#     yield 2
#     print("demo_in_3")
#     yield 3
#
#
# g = demo()  # 這時程式碼還不會被執行(處於閒置狀態)
# # print(g)  # => <generator object test at 0x000001DBC29FEF68>，生成器對象
# # 開始真正去調用生成器對象，會發現每調用一次__next__()，生成器就會運行到下一個yield的位置，然後再度進入閒置狀態
# print(g.__next__())  # => 1
# print('------------我是分隔線------------')
# print(g.__next__())  # => 2
# print('------------我是分隔線------------')
# print(g.__next__())  # => 3


# ------生成器表達式(生成器解析)------
# g = ("雞蛋%s" % i for i in range(10))  # => 使用小括號()
# # print(g)  # => <generator object <genexpr> at 0x000002606399EF68>，生成器對象
# for i in g:  # for循環可執行可迭代對象
#     print(i)


# ------生成器函數二------
# yield相當於return，控制的是函式返回值
# x = yeild 則是會接收send()的值並賦予給yeild
# def demo():
#     print("demo_in_1")
#     x = yield '回傳值1'
#     print("demo_in_2", x)
#     yield '回傳值1'
#
#
# import time
# res = demo()
# print(res.__next__())  # => 1
# time.sleep(2)
# # print(res.__next__())  # => 2
# print(res.send('傳值給yield'))  # => 2，傳值給yield讓x能接到值，並繼續執行到下個yield(相當於執行一個next())


# ------迭代器只能使用一次------
# li = (i for i in range(5))
# for i in li:
#     print(i, end='')  # => 01234
# for i in li:
#     print(i)   # => 啥都沒有(因為上個for已經把迭代器都循環過了一遍)
#
# print('\n------------我是分隔線------------')
# # 本質上不是迭代器則沒有此問題
# li = [1, 2, 3, 4, 5]
# for i in li:
#     print(i, end='')  # => 12345
# for i in li:
#     print(i, end='')   # => 12345，因為列表本質上不是迭代器


# ------生產者消費者模型------
# import time
# times = 0
#
#
# def consumer(i):
#     global times
#     print('我是%s，我要吃包子了' % i)
#     while True:
#         food = yield
#         times += 1
#         time.sleep(0.5)
#         print("我是%s，我把%s吃掉了【%s】" % (i, food, times))
#
#
# def producer(names):
#     for n in range(len(names)):
#         c = consumer(names[n])
#         c.__next__()  # 執行到while True下面的food = yield這行
#         for i in range(n*10, (n+1)*10):
#             time.sleep(0.1)
#             c.send("包子%s" % i)
#         time.sleep(1)
#
#
# producer(['jamie', 'sb'])
