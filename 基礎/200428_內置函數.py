# abs() 絕對值
# print(abs(-1))  # => 1

# all() 判斷全部元素是否都是True，但空的可跌代對象也會傳回True
# print(all([1, 2, "1"]))  # => True
# print(all([]))  # => True
# print(all(["", 1]))  # => False

# bin() 轉二進制
# print(bin(10))  # => 0b1010

# hex() 轉十六進制
# print(hex(10))  # => 0xa

# oct() 轉八進制
# print(oct(10))  # => 0o12

# bool() 判斷布林值
# print(bool(""))  # => False

# bytes() 編碼
# # 一個中文字佔三個字節
# print(bytes("你好", encoding='utf-8'))  # => b'\xe4\xbd\xa0\xe5\xa5\xbd'
# print("你好".encode('utf-8'))  # => b'\xe4\xbd\xa0\xe5\xa5\xbd'
# print(type(bytes("你好", encoding='utf-8')))  # => <class 'bytes'>
# # .decode("utf-8")解碼
# print(bytes("你好", encoding='utf-8').decode("utf-8"))  # => 你好

# chr() 根據ascii表找出對應值
# print(chr(97))  # => a

# dir() 查看函數屬性
# print(dir(all))
# print(dir(sum))

# divmod() 得出商和餘數
# print(divmod(10, 3))  # => (3, 1)

# eval()
# # 把字符串的數據結構提取出來
# s = '{"name": "jamie"}'
# print(type(s))  # => <class 'str'>
# print(eval(s), type(eval(s)))  # => {'name': 'jamie'} <class 'dict'>
# # 把字符串中的表達式進行運算
# s = '1*2+3'
# print(eval(s))  # => 5

# hash() 可hash的數據類型即不可變數據類型，不可則反(可用來判斷文件是否被更改過)
# name = "jamie"
# print(hash(name))  # => -6404532987003636270，不能根據hash值反推
# name = "sb"
# print(hash(name))  # => 7517366527548543912

# help() 查看函數使用方法
# print(help(all))

# isinstance() 判斷數據類型是否正確
# print(isinstance(1, int))  # => True

# globals() 找出全域變量
# name = "jamie"
# print(globals())

# locals() 找出當前級別的變量
# def foo():
#     name = "ddddddddddddddddddddddd"
#     print(locals())  # => {'name': 'ddddddddddddddddddddddd'}
# foo()

# zip() 拉鍊，前後序列一一對應
# res = zip(("a", "b", "c"), (1, 2, 3), ("一", "二", "三"))
# print(res, type(res))  # =>　<zip object at 0x0000016F27EBFEC8> <class 'zip'>
# print(list(res))  # => [('a', 1, '一'), ('b', 2, '二'), ('c', 3, '三')]
# print(list(zip(("a", "b", "c", "d"), (1, 2, 3))))  # => [('a', 1), ('b', 2), ('c', 3)]，"d"沒有對應值所以不顯示
# dic = {"name": "jamie", "age": 18, "gender": "boy"}
# print(list(zip(dic.keys(), dic.values())))  # => [('age', 18), ('name', 'jamie'), ('gender', 'boy')]
# print(dic.keys())  # => dict_keys(['gender', 'name', 'age'])
# print(dic.values())  # => dict_values(['boy', 'jamie', 18])

# max() 找最大值，參數須是可跌代對象，相當於用一個for循環取出每個元素(數據類型需相同)進行比較
# # 基礎用法
# print(max([1, -2, 10]))  # => 10
# age_dic = {"age1": 18, "age2": 28, "age3": 40, "age4": 100, "age100": 1000}
# print(max(age_dic.values()))  # => 1000
# print(max(age_dic))  # => age4，默認是keys()，字符串比較是從左到右從一個個元素開始比較，若有相等才比第二個
# print('--------------- 分隔線 ---------------')
# # 高階用法
# res = list(zip(age_dic.values(), age_dic.keys()))
# print(res)  # => [(40, 'age3'), (28, 'age2'), (18, 'age1'), (10, 'age100'), (100, 'age4')]
# print(max(res))  # => (100, 'age4')，默認從第一個元素開始比較，若有相等才比第二個，不同數據類型則不可比較
# print(max(age_dic, key=lambda key: age_dic[key]))  # => age4
# print('--------------- 分隔線 ---------------')
# # 高階用法二
# people = [
#     {"name": "jamie", "age": 18},
#     {"name": "sb", "age": 40},
#     {"name": "nb", "age": 100}
# ]
# print(max(people, key=lambda dic: dic["age"]))

# min() 找最小值
# 基礎用法
# print(min([1, -2, 10]))  # => -2
# 高階用法同max()

# ord() 跟chr()相反，根據字符找出ascii碼
# print(ord("a"))  # => 97

# pow()
# print(pow(10, 3))  # => 1000，10**3
# print(pow(10, 3, 6))  # => 4，(10**3)%6

# round() 四捨五入
# print(round(3.5))  # => 4

# slice() 切片
# s = "jamie"
# print(s[3:5])  # => ie
# print(s[slice(3, 5)])  # => ie
# print(s[slice(1, 4, 2)])  # => ai，s[1:4]且步長為2
# print(s[1:4:2])  # => ai

# sorted() 排序，不同類型不可排序
# # 基礎用法
# print(sorted([3, 5, 1]))  # => [1, 3, 5]
# # 高階用法
# people = [
#     {"name": "jamie", "age": 18},
#     {"name": "sb", "age": 40},
#     {"name": "nb", "age": 100}
# ]
# print(sorted(people, key=lambda dic: dic["age"]))
# # => [{'name': 'jamie', 'age': 18}, {'name': 'sb', 'age': 40}, {'name': 'nb', 'age': 100}]

# sum() 加總
# print(sum([1, 2, 3]))  # => 6

# type() 查看數據類型
# msg = "123"
# if type(msg) is str:
#     print(int(msg)+1)  # => 124

# vars() 將變量轉換成字典模式
# b = 1
# def foo():
#     msg = "jamie"
#     a = 10
#     print(vars())  # => {'a': 10, 'msg': 'jamie'}
# foo()

# # import------>system------>__import__
# # import 導入模塊(.py檔就是模塊)
# # import 180619_While迴圈
# module_name = "180619_While迴圈"
# m = __import__(module_name)  # 可以透過字符串類型導入模塊，且需設變數
