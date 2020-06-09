# -------數字int-------
# 1.數字轉為二進制所占用的bit數
a = 7
# print(a.bit_length())  # => 3
# 2.將字符串轉數字
# int("11")  # => 11 默認為十進制
# int("11", base=2)  # => 3
# int("a", base=16)  # => 10
# 3.創建連續數字(python2的xrange = python3的range)
# range(0, 100) = range(100)  # 0-99
# range(0, 100, 5) # 0,5,10...,90,95

# -------字符串str------- (一旦創建，就不能修改；一旦修改，就會創建新的字符串。)
name = "jamieooo"
# 1.轉大寫
# print(name.upper())  # => JAMIEOOO
# print(name.isupper())  # => False 判斷是否為大寫
# 2.轉小寫
# print(name.casefold())  # => jamieooo 不只能轉換英文大小寫
# print(name.lower())  # => jamieooo
# print(name.islower())  # => True 判斷是否為小寫
# 3.首字母大寫
# print(name.capitalize())  # => Jamieooo
# 4.設置寬度將內容填滿，後面的"~"則表示空格處用~填滿
# print(name.center(20, "~"))  # => ~~~~~~jamieooo~~~~~~ 置中填滿
# print(name.ljust(20, "*"))  # => jamieooo************ 左填滿
# print(name.rjust(20, "*"))  # => ************jamieooo 右填滿
# 5.計算在字符串內出現的次數
# print(name.count("o"))  # => 3
# print(name.count("i", 2, 4))  # => 1 從name[2]到name[4-1]中找值
# 6.判斷是否為結尾字符串
# print(name.endswith("o"))  # => True
# 7.判斷是否為開頭字符串
# print(name.startswith("ja"))  # => True
# 8.找出第一個欲查詢值所在的位置，沒找到回傳-1
# print(name.find("o"))  # => 5
# print(name.find("i", 2, 4))  # => 3 從name[2]到name[4-1]中找
# print(name.rfind("o"))  # => 7 從後面開始找
# 9.格式化，將字符串中的占位符替換成指定值
# test = "I am {name}, age = {age}"
# print(test.format(name = "jamie", age = 22))  # => I am jamie, age = 22
# print(test.format(**{"name": "jamie", "age": 22}))  # => I am jamie, age = 22  **kwargs
# print(test.format_map({"name":"jamie", "age":22}))  # => I am jamie, age = 22
# 10.判斷字符串中是否只包含數字、字母和漢字
# print(name.isalnum())  # => True
# 11.判斷字符串中是否只包含字母和漢字
# print(name.isalpha())  # => True
# 12.判斷字符串中是否只包含數字(不能是小數，因為會包含符號.)
# print(name.isdigit())  # => False
# 13.將字符串斷句，每10個為一組，若遇到\t直接用空格補到10，可用來排版
# test = "name\tage\tbirthday\njamie\t22\t851230\njamie\t22\t851230\njamie\t22\t851230\n"  # \n換行
# print(test.expandtabs(10))
# 14.判斷是否全為能打印之字符(不能打印的：不可顯示的字符\n\t)
# test = "不可顯示的字符\n"
# print(test.isprintable())  # => False
# 15.判斷是否為全空格字串
# print("\t\n".isspace())  # => True
# print(name.isspace())  # => False
# 16.將字符串每個字符依指定分隔符拼接
# test = "你是風兒我是沙"
# print("~".join(test))  # => 你~是~風~兒~我~是~沙
# print("~".join(["你是", "風", "兒"]))  # => 你是~風~兒
# print("".join(["你是", "風", "兒"]))  # => 你是風兒
# 17.分割字符串
# print(name.partition("o"))  # => ('jamie', 'o', 'oo') 只能分割第一個(三份)，且保留分割字元
# print(name.split("o"))  # => ['jamie', '', '', ''] 全分割，且不保留分割字元
# print(name.split("o", 2))  # => ['jamie', '', 'o'] 前兩個指定符分割，且不保留分割字元
# 18.替代字符
# print(name.replace("o", "e"))  # => jamieeee
# print(name.replace("o", "e", 1))  # => jamieeoo  只替換第一個
# 19.索引
# print(name[1])  # => a
# print(name[1:3])  # => am  name[1]到name[3-1]
# print(name[1:6:2]) # => aio  name[1]到name[6-1]，步長為2
# 20.計算字符串長度
# print(len(name))  # => 8
# 21.for迴圈打印字串(表字符串可經過for轉換為可迭代對象)
# test = "你是風兒我是沙"
# for i in test:
#     print(i)
# 22.列表轉字符串(不能直接用str(li))
# li = ["我", 1, 2, 3]
# s = ""
# for i in li:
#     s = s + str(i)
# print(s)  # => 我123
# 23.去除首尾字符，默認是去除空白和迴車
# name = "---s-b---------------"
# print(name.strip("-"))  # => s-b
# 24.重複字符串
# print('jamie'*3)  # => jamiejamiejamie

# -------列表list-------(列表中的元素可以是數字、字符串、列表、字典等，有序且可以修改，存取方法類似於c的link list)
# 1.for迴圈打印列表(表列表可經過for轉換為可迭代對象)
# li = ["我", 2, 3, 5]
# for i in li:
#     print(i)
# 2.刪除指定位置元素
# li = ["我", 2, 3, 5]
# del li[0]
# print(li)  # => [2, 3, 5]
# del li[0:3]
# print(li)  # => [5]
# 3.判斷是否包含該元素
# li = ["我", 2, 3, 5, ["你", "他"]]
# print(["你", "他"] in li)  # => True
# print("你" in li)  # => False
# 4.字符串轉列表
# test = "abcdefg"
# print(list(test))  # => ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# num = 123
# print(list(num))  # => Error，因為數字不可被迭代
# 5.在列表的最後新增元素
# li = ["我", 2, 3, 5, ["你", "他"]]
# li.append([10, "挖"])
# print(li)  # => ['我', 2, 3, 5, ['你', '他'], [10, '挖']]
# 6.清空列表
# li = ["我", 2, 3, 5, ["你", "他"]]
# li.clear()
# print(li)  # => []
# 7.複製(淺)
# li = ["我", 2, 3, 5, ["你", "他"]]
# li2 = li.copy()
# print(li2)  # => ['我', 2, 3, 5, ['你', '他']]
# 8.計算元素出現次數
# li = ["我", 2, 3, 5, ["你", "他", 2]]
# print(li.count(2))  # => 1
# 9.在列表的最後新增元素
# li = ["我", 2, 3, 5, ["你", "他", 2]]
# li.extend([10, "挖"])  # 參數須可迭代(字符串、列表...)
# print(li)  # => ['我', 2, 3, 5, ['你', '他', 2], 10, '挖']
# 10.找出第一個符合元素的索引位置
# li = ["我", 2, 3, 5, ["你", "他", 2], 2]
# print(li.index(2))  # => 1
# 11.在指定索引位置新增元素
# li = ["我", 2, 3, 5, ["你", "他", 2]]
# li.insert(0, 99)
# print(li)  # => [99, '我', 2, 3, 5, ['你', '他', 2]]
# 12.根據索引位置刪除元素，並取得被刪除元素
# li = ["我", 2, 3, 5, ["你", "他", 2]]
# v = li.pop(1)  # 默認刪最後一個，此刪除li[1]
# print(li)  # => ['我', 3, 5, ['你', '他', 2]]
# print(v)  # => 2  被刪除的值
# 13.根據字面量，刪除第一個指定元素
# li = ["我", 2, 3, 5, ["你", "他", 2], 2]
# li.remove(2)
# print(li)  # => ['我', 3, 5, ['你', '他', 2], 2]
# 14.反轉列表
# li = [1, 2, 3, 4]
# li.reverse()
# print(li)  # => [4, 3, 2, 1]
# 15.排序列表
# li = [5, 99, 2, 88, 87]
# li.sort()
# print(li)  # => [2, 5, 87, 88, 99]
# li.sort(reverse=True)
# print(li)  # => [99, 88, 87, 5, 2]

# -------元組tuple-------(元素不可被修改、新增、刪除，有序)
# 1.for迴圈打印元組(表元組可經過for轉換為可迭代對象)
# tu = (11, 22, 33, 44,)  # 在最後加個逗號，用來區別方法和元組
# for i in tu:
#     print(i)
# 2.元組轉字符串
# tu = (11, 22, 33, 44,)
# print(list(tu))  # => [11, 22, 33, 44]
# 3.獲取指定元素的出現次數
# tu = (11, 22, 33, 44, 22)
# print(tu.count(22))  # => 2
# 4.獲取第一個指定元素索引位置
# tu = (11, 22, 33, 44, 22)
# print(tu.index(22))  # => 1

# -------字典dict-------(字典的value可以是任何類型，布林值、列表、字典不能做為key，無序)
# 1.基本練習，找到11
# di = {"k1": 18, "k2": True, "k3": [13, 22, 33, {"kk1": (11, 22)}], "k4": (13, 22)}  # 元素為鍵值對
# print(di["k3"][3]["kk1"][0])  # => 11
# 2.刪除鍵值對
# di = {"k1": 18, "k2": True, "k3": [13, 22, 33, {"kk1": (11, 22)}], "k4": (13, 22)}  # 元素為鍵值對
# del di["k1"]
# print(di)  # => {'k2': True, 'k4': (13, 22), 'k3': [13, 22, 33, {'kk1': (11, 22)}]}
# 3.for迴圈打印字典(表字典是可迭代對象)
# di = {"k1": 18, "k2": True, "k3": [13, 22, 33, {"kk1": (11, 22)}], "k4": (13, 22)}
# for i in di:
#     print(i)  # => k4,k1,k3,k2 默認打印key
# di = {"k1": 18, "k2": True, "k3": [13, 22, 33, {"kk1": (11, 22)}], "k4": (13, 22)}
# for i in di.values():
#     print(i)  # value
# di = {"k1": 18, "k2": True, "k3": [13, 22, 33, {"kk1": (11, 22)}], "k4": (13, 22)}
# for k, v in di.items():
#     print(k, v)  # => key + value
# 4.根據序列創建字典，並指定統一的值(此為靜態方法，調用方法為 類.方法())
# print(dict.fromkeys([1, 2, 3], 123))  # => {1: 123, 2: 123, 3: 123}
# 5.根據key獲取值(比di["k1"]方法好，因為沒找到key不會error)
# di = {"k1": 18, "k2": True, "k3": [13, 22, 33, {"kk1": (11, 22)}], "k4": (13, 22)}
# v = di.get("k1", "不存在")  # 參數一為要找的key值、參數二為當找不到key時回傳的文字
# print(v)  # => 18
# v = di.get("k1111", "不存在")  # 參數一為要找的key值、參數二為當找不到key時回傳的文字
# print(v)  # => 不存在
# v = di.get("k1111")  # 參數一為要找的key值、參數二為當找不到key時回傳的文字
# print(v)  # => None
# 6.刪除鍵值對，並回傳被刪除的value
# di = {"k1": 18, "k2": True, "k3": [13, 22, 33, {"kk1": (11, 22)}], "k4": (13, 22)}
# v = di.pop("k1", 90)  # 參數二為默認值，若找不到key刪除，則pop()回傳默認值
# print(di)  # => {'k4': (13, 22), 'k3': [13, 22, 33, {'kk1': (11, 22)}], 'k2': True}
# print(v)  # => 18
# 7.新增鍵值對，若key不存在則直接新增且回傳value，若key已存在則不新增且回傳原本的value
# di = {"k1": 18, "k2": True}
# v = di.setdefault("k3", 4)
# print(di, v)  # => {'k2': True, 'k3': 4, 'k1': 18} 4
# v = di.setdefault("k2", 4)
# print(di, v)  # => {'k1': 18, 'k2': True} True
# 8.更新鍵值對
# di = {"k1": 18, "k2": True}
# di.update({"k1": 11111, "k3": 123})
# print(di)  # => {'k2': True, 'k1': 11111, 'k3': 123}
# 9.字典清空
# di = {"k1": 18, "k2": True}
# di.clear()
# print(di)  # => {}
# 10.字典複製
# di = {"k1": 18, "k2": True}
# di2 = di.copy()
# print(di2)  # => {'k1': 18, 'k2': True}


# -------布林值bool-------
# 默認表示False = 0, True = 1
# None, "", (), [], {}, 0 => 這些都是False，其他為True


# -------集合set-------
# 1.不會有相同的元素，所以重複的會被去除
# s = {1, 2, 3, 3, 3}
# print(s)  # => {1, 2, 3}
# 2.創建集合
# s = set("hello")
# print(s)  # => {'h', 'l', 'o', 'e'}
# s = set(["jamie", "jamie", "sb"])
# print(s)  # => {'jamie', 'sb'}
# 3.新增元素
# s = {1, 2, 3, 3, 3}
# s.add("3")
# print(s)  # => {'3', 1, 2, 3}  # 不同數據類型的3算不同元素
# 4.刪除隨機元素
# s = {"s", 1, 2, 3, 3, 3, 4}
# s.pop()
# print(s)  # => {2, 3, 4, 's'}
# 5.刪除指定元素
# s = {"s", 1, 2, 3, 3, 3, 4}
# s.remove("s")  # 若刪除元素不存在會報錯
# print(s)  # => {1, 2, 3, 4}  #
# s = {"s", 1, 2, 3, 3, 3, 4}
# s.discard("s")  # 若刪除元素不存在不會報錯
# print(s)  # => {1, 2, 3, 4}

# 集合關係運算
li1 = ["a", "b", "c"]
li2 = ["a", "b", "d"]
# 列表轉集合，有序=>無序
s1 = set(li1)
s2 = set(li2)
# 交集
# print(s1.intersection(s2))  # => {'b', 'a'}
# print(s1&s2)  # => {'b', 'a'}
# 聯集
# print(s1.union(s2))  # => {'c', 'b', 'a', 'd'}
# print(s1|s2)  # => {'c', 'b', 'a', 'd'}
# 差集
# print(s1.difference(s2))  # => {'c'}
# print(s1-s2)  # => {'c'}
# print(s2-s1)  # => {'d'}
# 交叉補集(聯集-交集)
# print(s1.symmetric_difference(s2))  # => {'c', 'd'}
# print(s1^s2)  # => {'c', 'd'}
# 判斷是否交集
# print(s1.isdisjoint(s2))  # => False
# 判斷是否是子集合
# test = {1, 2, 3}
# test2 = {1, 2}
# print(test.issubset(test2))  # => False
# print(test2.issubset(test))  # => True  test2是test的子集合



