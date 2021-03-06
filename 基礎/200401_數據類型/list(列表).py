# -------列表list-------(列表中的元素可以是數字、字符串、列表、字典等，有序且可以修改，存取方法類似於c的link list)

# for迴圈打印列表(表列表可經過for轉換為可迭代對象)
# li = ["我", 2, 3, 5]
# for i in li:
#     print(i)

# 刪除指定位置元素
# li = ["我", 2, 3, 5]
# del li[0]
# print(li)  # => [2, 3, 5]
# del li[0:2]  # 刪除li[0]到li[2]
# print(li)  # => [5]

# 判斷是否包含該元素
# li = ["我", 2, 3, 5, ["你", "他"]]
# print(["你", "他"] in li)  # => True
# print("你" in li)  # => False

# 字符串轉列表
# test = "abcdefg"
# print(list(test))  # => ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# num = 123
# print(list(num))  # => Error，因為數字不可被轉換為迭代對象

# 在列表的最後新增元素
# li = ["我", 2, 3, 5, ["你", "他"]]
# li.append([10, "挖"])
# print(li)  # => ['我', 2, 3, 5, ['你', '他'], [10, '挖']]

# 清空列表
# li = ["我", 2, 3, 5, ["你", "他"]]
# li.clear()
# print(li)  # => []

# 複製
# li = ["我", 2, 3, 5]
# li2 = li.copy()
# print(li2)  # => ['我', 2, 3, 5]
# li.append(1)
# print(li2)  # => ['我', 2, 3, 5]

# 計算元素出現次數
# li = ["我", 2, 3, 5, ["你", "他", 2]]
# print(li.count(2))  # => 1

# 在列表的最後新增元素(可一次新增多個)
# li = ["我", 2, 3, 5, ["你", "他", 2]]
# li.extend([10, "挖"])  # 參數須可迭代(字符串、列表...)
# print(li)  # => ['我', 2, 3, 5, ['你', '他', 2], 10, '挖']

# 找出第一個符合元素的索引位置
# li = ["我", 3, 5, ["你", "他", 2], 3, 2, 2]
# print(li.index(2))  # => 5

# 在指定位置新增元素
# li = ["我", 2, 3, 5, ["你", "他", 2]]
# li.insert(0, 99)
# print(li)  # => [99, '我', 2, 3, 5, ['你', '他', 2]]

# 根據索引刪除元素，並取得被刪除元素
# li = ["我", 2, 3, 5, ["你", "他", 2]]
# v = li.pop(1)  # 默認刪最後一個，此刪除li[1]
# print(li)  # => ['我', 3, 5, ['你', '他', 2]]
# print(v)  # => 2  被刪除的值

# 根據值刪除第一個指定元素
# li = ["我", 2, 3, 5, ["你", "他", 2], 2]
# li.remove(2)
# print(li)  # => ['我', 3, 5, ['你', '他', 2], 2]

# 反轉列表
# li = [1, 2, 3, 4]
# li.reverse()
# print(li)  # => [4, 3, 2, 1]

# 排序列表
# li = [5, 99, 2, 88, 87]
# li.sort()
# print(li)  # => [2, 5, 87, 88, 99]
# li.sort(reverse=True)
# print(li)  # => [99, 88, 87, 5, 2]
