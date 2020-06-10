"""
windows默認 r = rt, w = wt, a = at，t為文本(text)模式
r唯讀、w唯寫(新建並覆蓋原檔)、a附加(寫到文件最後)，默認是r
"""

# 1.r唯讀 w唯寫(新建並覆蓋原檔) a附加(寫到文件最後)，默認是r
# f = open('筆記.txt', encoding='utf-8')  # 預設路徑為當前資料夾，後面加上解碼方式
# data = f.read()  # 讀取全部
# print(data)
# f.close()  # 關掉後data還是會存在於內存
# print('---------------------- 我是分隔線 ----------------------')
# print(data)

# 2.readline() 一次讀一行，包含換行
# f = open('筆記.txt', 'r', encoding='utf-8')
# print(f.readable())  # => True，返回是否可讀
# print('第1行', f.readline(), end="")  # => 開發：
# print('第2行', f.readline(), end="")  # => 高階語言：Java, python, c#, php, c++...   ==> 轉字節碼
# f.close()
# # print('第3行', f.readline(), end="") # 關閉文件後就不能再次訪問

# 3.readlines() 把每一行讀出來並加到陣列中
# f = open('筆記.txt', 'r', encoding='utf-8')
# data = f.readlines()
# print(data)
# f.close()

# 4.'w' 文件不管是否存在，都是新建並覆蓋原檔
# f = open('test.txt', 'w', encoding='utf-8')
# f.write("111111\n")  # 不會自動換行，要自己加
# f.write("222222\n")
# f.close()

# 5.writelines() 參數為列表
# f = open('test.txt', 'w', encoding='utf-8')
# f.writelines(['1111\n', '2222\n', '拉拉阿\n'])
# # f.writelines(['1111\n', '2222\n', 1])  # => 報錯，文件內容必須是字符串
# f.close()

# 6.'a'寫文字到文件最後
# f = open('test2.txt', 'a', encoding='utf-8')
# f.write("aaaaa\n")
# f.close()

# 7.'r+' = 可讀可寫(寫在鼠標停的位置，默認在開頭)
# f = open('test2.txt', 'r+', encoding='utf-8')
# f.write("使用r+覆蓋\n")  # 會把第一行的部分文字覆蓋掉，因為鼠標在開頭，且文件不可修改只能覆蓋
# f.close()

# 8.修改文件
# f = open('test.txt', 'r', encoding='utf-8')
# data = f.readlines()
# f.close()
#
# d = open('test.txt', 'w', encoding='utf-8')
# d.write(data[0])  # 只保留第一行
# d.close()

# 9.使用with打開，會自動close()
# with open('test.txt', 'w', encoding='utf-8') as f:
#     f.write("www")

# 10.with多開
# # \ => 程式換行
# with open('test.txt', 'r', encoding='utf-8') as f,\
#     open('test2.txt', 'w', encoding='utf-8') as d:
#     data = f.readlines()
#     d.write(data[0])  # 只保留第一行

# 11.rb，b模式 => 字節(二進制)模式
# with open('test.txt', 'rb') as f:   # b不能指定編碼
#     data = f.read()
#     # bytes
#     print(data)
#     # bytes ======> 字符串
#     print(data.decode('utf-8'))

# 12.wb
# with open("test.txt", 'wb') as f:
#     x = 'hello\n'
#     print(type(x))  # => <class 'str'>
#     f.write(bytes(x, encoding='utf-8'))  # 通過bytes轉
#     print(type(bytes(x, encoding='utf-8')))  # => <class 'bytes'>
#
#     f.write(b'hello2\n')  # 直接寫入字節

# 其他用法
# f = open('test.txt', 'r+', encoding='utf-8')
# print(f.closed)  # => False，判斷文件是否關閉
#
# print(f.encoding)  # => utf-8，程式打開文件時用的編碼(不是文件本身的編碼)
#
# print(f.tell())  # => 0，鼠標目前位置(以字節計算)
# f.seek(5)  # => 控制鼠標位置(以字節計算)
# print(f.tell())  # => 5(以字節計算)
#
# data = f.read(5)  # 讀取5個字符(以字符計算)
# print(data)
#
# f.truncate(9)   # 截斷，只保留前九個字節(以字節計算)

