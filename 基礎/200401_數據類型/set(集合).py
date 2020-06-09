"""
集合：
    1. 不同元素組成
    2. 無序
    3. 元素須為不可變類型 => 字符串、數字、元組
    4. 本身是可變類型，除非定義不可變集合(EX:s = frozenset("hello"))
    5. 可迭代
"""

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
