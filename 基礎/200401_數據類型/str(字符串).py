# -------字符串str------- (一旦創建，就不能修改；一旦修改，就會創建新的字符串。)
name = 'jamieooo'

# 英文大寫
# print(name.upper())  # => JAMIEOOO
# print(name.isupper())  # => False 判斷是否為大寫

# 英文小寫
# print(name.casefold())  # => jamieooo 不只能轉換英文大小寫
# print(name.lower())  # => jamieooo
# print(name.islower())  # => True 判斷是否為小寫

# 首字母大寫
# print(name.capitalize())  # => Jamieooo

# 設置寬度將內容填滿，後面的"~"則表示空格處用~填滿
# print(name.center(20, "~"))  # => ~~~~~~jamieooo~~~~~~ 置中填滿
# print(name.ljust(20, "*"))  # => jamieooo************ 左填滿
# print(name.rjust(20, "*"))  # => ************jamieooo 右填滿

# 計算在字符串內出現的次數
# print(name.count("o"))  # => 3
# print(name.count("i", 2, 4))  # => 1 從name[2]到name[4-1]中找出現次數

# 判斷是否為結尾字符串
# print(name.endswith("o"))  # => True

# 判斷是否為開頭字符串
# print(name.startswith("ja"))  # => True

# 找出第一個欲查詢值所在的位置，沒找到回傳-1
# print(name.find("o"))  # => 5
# print(name.find("i", 2, 4))  # => 3 從name[2]到name[4-1]中找值
# print(name.rfind("o"))  # => 7 從後面往回找

# 格式化，將字符串中的占位符替換成指定值
# test = "I am {name}, age = {age}"
# print(test.format(name="jamie", age=22))  # => I am jamie, age = 22
# print(test.format(**{"name": "jamie", "age": 22}))  # => I am jamie, age = 22  **kwargs
# print(test.format_map({"name": "jamie", "age": 22}))  # => I am jamie, age = 22
# test2 = "I am {0}, age = {0}"
# print(test2.format('87'))  # => I am 87, age = 87

# 判斷字符串中是否只包含數字、字母和漢字
# test = '陳俊宇jamie851230'
# print(test.isalnum())  # => True

# 判斷字符串中是否只包含字母和漢字
# test = '陳俊宇jamie851230'
# print(test.isalpha())  # => False
# test = '陳俊宇jamie'
# print(test.isalpha())  # => True

# 判斷字符串中是否只包含數字(不能包含符號)
# test = '851230'
# print(test.isdigit())  # => True
# test = '87.87'
# print(test.isdigit())  # => False
# test = '-87'
# print(test.isdigit())  # => False

# 將字符串斷句，每10個為一組，若遇到\t直接用空格補到10，可用來排版
# test = "name\tage\tbirthday\njamie\t22\t851230\nsb\t22\t87\njamie\t22\t851230\n"  # \n換行
# # print(test.expandtabs(10))
'''
name      age       birthday
jamie     22        851230
sb        22        87
jamie     22        851230
'''

# 判斷是否能打印(不能打印的：不可顯示的字符\n\t\r)
# test = "不可顯示的字符\n"
# print(test.isprintable())  # => False
# test = "不可顯示的字符\r"
# print(test.isprintable())  # => False

# 判斷是否為全空格字串
# print("\t\n\r".isspace())  # => True
# print(" ".isspace())  # => True
# print(name.isspace())  # => False

# 將字符串每個字符依指定分隔符拼接
# test = "你是風兒我是沙"
# print("~".join(test))  # => 你~是~風~兒~我~是~沙
# print("~".join(["你是", "風", "兒"]))  # => 你是~風~兒
# print("".join(["你是", "風", "兒"]))  # => 你是風兒

# 分割字符串
# print(name.partition("o"))  # => ('jamie', 'o', 'oo') 只能分割第一個值，分成三份且保留分割字元
# print(name.split("o"))  # => ['jamie', '', '', ''] 全分割，且不保留分割字元
# print(name.split("o", 2))  # => ['jamie', '', 'o'] 前兩個指定符分割，且不保留分割字元
# print(name.rsplit("o", 2))  # => ['jamieo', '', ''] 從後面往回分割

# 替代字符
# print(name.replace("o", "e"))  # => jamieeee
# print(name.replace("o", "e", 1))  # => jamieeoo  只替換第一個

# 索引
# print(name[1])  # => a
# print(name[1:3])  # => am  name[1]到name[3-1]
# print(name[1:6:2]) # => aio  name[1]到name[6-1]，步長為2

# 計算字符串長度
# print(len(name))  # => 8

# for迴圈打印字串(表字符串可經過for轉換為可迭代對象)
# test = "你是風兒我是沙"
# for i in test:
#     print(i)

# 列表轉字符串(不能直接用str(li))
# li = ["我", 1, 2, 3]
# s = ""
# for i in li:
#     s = s + str(i)
# print(s)  # => 我123
# print(str(li))  # => '['我', 1, 2, 3]'

# 去除首尾字符，默認是去除空白和迴車
# test = "---s-b---------------"
# print(test.strip("-"))  # => s-b
# print(test.lstrip("-"))  # => s-b---------------
# print(test.rstrip("-"))  # => ---s-b

# 重複字符串
# print('jamie'*3)  # => jamiejamiejamie
# print("-"*20)  # => --------------------
