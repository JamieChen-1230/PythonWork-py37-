# ------------ 百分比字符串格式化 ------------
# %s可放字符串、數字、列表、字典
# msg = "I am %s" % "Jamie"
# print(msg)  # => I am Jamie
# msg = "I am %s" % [1, 2, 3]
# print(msg)  # => I am [1, 2, 3]

# 多個%s
# name = "Jamie"
# msg = "I am %s, my hobby is %s." % (name, "sleeping")
# print(msg)  # => I am Jamie, my hobby is sleeping.

# %d只可放整數
# print("age is %d" % 18)  # age is 18
# print("age is %d" % 18.88)  # age is 18

# %f浮點數
# print("percent %f" % 1.123456)  # => percent 1.123456
# print("percent %.2f" % 1.123456)  # => percent 1.12，只保留小數點後兩位

# 用字典傳值
# msg = "I am %(name)s, my hobby is %(hobby)s." % {"name": "Jamie", "hobby": "sleeping"}
# print(msg)  # => I am Jamie, my hobby is sleeping.

# flags, width
# msg = "I am %(name)-10s, my hobby is %(hobby)s." % {"name": "Jamie", "hobby": "sleeping"}
# print(msg)  # => I am Jamie     , my hobby is sleeping. 左對齊且寬度為10
# msg = "I am %(name)+10s, my hobby is %(hobby)s." % {"name": "Jamie", "hobby": "sleeping"}
# print(msg)  # => I am      Jamie, my hobby is sleeping. 右對齊且寬度為10

# print分隔符
# print(1, 2, 3, 4, sep=":")  # => 1:2:3:4  sep不設定默認為" "


# ------------ format字符串格式化 ------------
# msg = "I am {}, age is {}, {}".format("Jamie", 18, "sb")
# print(msg)  # => I am Jamie, age is 18, sb

# 標數字 => 對應元組索引位置
# msg = "I am {2}, age is {1}, {0}".format("Jamie", 18, "sb")
# print(msg)  # => I am sb, age is 18, Jamie
# msg = "I am {2}, age is {2}, {2}".format("Jamie", 18, "sb")
# print(msg)  # => I am sb, age is sb, sb

# 使用鍵值對形式傳值
# msg = "I am {name}, age is {age}".format(name = "Jamie", age = 18)
# print(msg)  # => I am Jamie, age is 18
# msg = "I am {name}, age is {age}".format(**{"name": "Jamie", "age": 18})
# print(msg)  # => I am Jamie, age is 18

# 元組內元素為列表
# msg = "I am {0[2]}, age is {1[1]}".format(["Jamie", "JJ", "sb"], [11, 22, 33])
# print(msg)  # => I am sb, age is 22

# 使用列表形式傳值
# msg = "I am {0}, age is {1}".format(*["Jamie", 18])
# print(msg)  # => I am Jamie, age is 18

# 設定不同數字類型
# msg = "number: {:b}, {:o}, {:d}, {:x}, {:%}".format(15, 15, 15, 15, 15.87878787)
# print(msg)  # => number: 1111, 17, 15, f, 1587.878787%，二進制, 八進制, 整數, 十六進制, 百分比
