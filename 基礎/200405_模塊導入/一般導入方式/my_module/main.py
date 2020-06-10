"""
主程式：
    - 必須加上from my_module，因為路徑是由執行文件所產稱的，
    - 而我們的執行文件為bin.py而不是main.py，
    - 故路徑是停在「一般導入方式」這層資料夾，要調用add.py需加上from my_module
"""

# (1)
# from my_module import add
# def run():
#     print(add.add(3, 7))
# (2)
# from my_module.add import add
# def run():
#     print(add(3, 8))

from my_module import add
