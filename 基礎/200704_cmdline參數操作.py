import sys
import getopt

# ※ 使用時一般參數要放在帶"-"或"--"的參數之後
# 使用範例： python 200704_cmdline參數操作.py -a aaaa -b --start 20200101 --end 20200501 jamie 18 190

print('參數個數: ' + str(len(sys.argv)))  # => 11
print('參數列表: ' + str(sys.argv))
# => ['200704_cmdline參數操作.py', '-a', 'aaaa', '-b', '--start', '20200101', '--end', '20200501', 'jamie', '18', '190']


# 使用getopt更細的篩選參數
# getopt.getopt(<參數列表>, <帶"-"的參數>, [<帶"--"的參數>])
#   帶"-"的參數： "a:bc:"，這樣表示a和c(後面有加":"的參數)後面要跟一個值，而b不用，所以像b這種通常用來當作開關參數
#   帶"--"的參數： ["start=", "end="]，這樣表示start和end(後面有加"="的參數)後面要跟一個值，而delete不用，所以常用來作開關參數
opts, args = getopt.getopt(sys.argv[1:], "a:bc:", ["start=", "end=", "delete"])

# opts用來接收帶"-"或"--"的參數和它後面跟的值
# args用來接收一般參數
# ※ 使用時一般參數要放在帶"-"或"--"的參數之後
print("opts: ", opts)  # => [('-a', 'aaaa'), ('-b', ''), ('--start', '20200101'), ('--end', '20200501')]
print("args: ", args)  # => ['jamie', '18', '190']

# 之後使用：
# 可以通過迴圈和if判斷，來判定當接收到這個參數時要如何使用
for key, val in opts:
    if key == "-a":
        print("-a: ", val)
    if key == '-b':
        print('bbbb')


