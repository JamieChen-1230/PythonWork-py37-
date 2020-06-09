# -------布林值bool-------

# 默認表示False = 0, True = 1
# None, "", (), [], {}, 0 => 這些都是False，其他為True
print(bool("d"))  # => True
print(bool(" "))  # => True
print(bool(""))  # => False
print(bool("0"))  # => True
print(bool(0))  # => False
print(bool([]))  # => False
