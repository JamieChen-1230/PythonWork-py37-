"""
模塊： 一個.py文件就是一塊模塊
    - 使用模塊可以避免函數名和變量名相同和發生衝突(不同模塊間可以有相同的函數名和變量名)
"""

# 使用import： (1) 會把導入的模塊先執行一遍 (2) 引入模塊變量名
# import cal   # 導入同層級下的cal模塊，並導入cal裡面的方法變量名
# print(cal.add(3, 5))  # => 8
# print(cal.sub(3, 5))  # => -2


# 這種方式能直接調用函數名
# from cal import add, sub
# from cal import *  # *代表導入全部，但有可能會導致函數名重複而被覆蓋(因為本身不知導入了那些函數)
# print(add(3, 5))  # => 8
# print(sub(3, 5))  # => -2


# 要導入不同地方的模塊，導入時會從以下路徑去尋找被調用文件
# import sys
# print(sys.path)
# ['D:\\PythonWork\\SelfLearn\\基礎\\180715_模塊介紹',   # 當前執行文件路徑
# 'D:\\PythonWork',  # pycharm提供的(但盡量不要使用)
# 'D:\\Python35\\python35.zip',  # 剩下都是內建的
# 'D:\\Python35\\DLLs',
# 'D:\\Python35\\lib',
# 'D:\\Python35',
# 'C:\\Users\\USER\\AppData\\Roaming\\Python\\Python35\\site-packages',
# 'D:\\Python35\\lib\\site-packages', 'D:\\Python35\\lib\\site-packages\\win32',
# 'D:\\Python35\\lib\\site-packages\\win32\\lib',
# 'D:\\Python35\\lib\\site-packages\\Pythonwin']
# # 因為目前路徑只到「一般導入方式」這層資料夾，所以需加入my_module.my_module2才能到my_module2去找cal2
# from my_module.my_module2 import cal2
# print(cal2.add(3, 5))  # => 8


# 程式接口、起始文件(拿來運行的py檔) ==> bin.py
#         主程式           ==> main.py
#      其他功能模塊        ==> EX：add.py

# __name__
# 最常用法一 if __name__ == "__main__": -----> 讓程序文件被調用時不會執行以下代碼(用於測試代碼，這樣就不須註解掉測試碼)
# 最常用法二 if __name__ == "__main__": -----> 用於主執行文件且不想讓別人調用時可以使用
# print(__name__)  # => __main__，因在執行文件中打印
# from my_module import name_test
# name_test.name()  # => my_module.name_test，在調用文件中打印

# 調用上一級的資料夾與模塊
# import os, sys
# if __name__ == "__main__":
#     # 文件絕對路徑
#     # => D:/Programming/WorkPlace/PythonWork(py37)/基礎/180715_模塊基本架構介紹/一般導入方式/模塊基本架構介紹.py
#     print(os.path.abspath(__file__))
#     # 跳到上一級
#     # => D:\Programming\WorkPlace\PythonWork(py37)\基礎\180715_模塊基本架構介紹\一般導入方式
#     print(os.path.dirname(os.path.abspath(__file__)))
#     # 跳到上兩級
#     # => D:\Programming\WorkPlace\PythonWork(py37)\基礎\180715_模塊基本架構介紹
#     print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#
#     BASE_DIR = sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 把目錄加入sys.path
#     # 這樣就能調用 D:\Programming\WorkPlace\PythonWork(py37)\基礎\180715_模塊基本架構介紹 目錄上的東西了


