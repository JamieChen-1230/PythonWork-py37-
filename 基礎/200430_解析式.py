"""列表解析(列表推導)"""
'''求一包含1-10平方根的陣列'''
# 一般作法
# li = []
# for i in range(1, 11):
#     num = i ** 0.5
#     li.append(num)
# print(li)

# 列表解析
# 前半部分 i**0.5 => 表示要對每個i做的處理(表達式)
# 後半部分 for i in range(1, 11) => 表i要從哪裡跌代(循環)
# li = [i**0.5 for i in range(1, 11)]  # 生成一個列表
# print(li)

'''求一5以內的單數和5以內的雙數的組合列表'''
# 一般作法
# li = []
# for odd in range(1, 6):
#     if odd % 2 == 1:
#         for even in range(1, 6):
#             if even % 2 == 0:
#                 li.append((odd, even))
# print(li)

# 列表解析
# 方式一(較優，循環次數較少)
# li = [(odd, even)
# #       for odd in range(1, 6)
# #       if odd % 2 == 1
# #       for even in range(1, 6)
# #       if even % 2 == 0
# #       ]
# # print(li)

# 方式二
# li = [(odd, even)
#       for odd in range(1, 6)
#       for even in range(1, 6)
#       if odd % 2 == 1
#       if even % 2 == 0
#       ]
# print(li)

"""集合解析式(集合內之元素必須為hashable，list和dict不為hashable)"""
# se = {(odd, even)
#        for odd in range(1, 6)
#        if odd % 2 == 1
#        for even in range(1, 6)
#        if even % 2 == 0
#       }
# print(se)

"""字典解析式(前半部分表達式必須為 key:value 形式，key必須為hashable)"""
# dic = {odd: even
#        for odd in range(1, 6)
#        if odd % 2 == 1
#        for even in range(1, 6)
#        if even % 2 == 0
#       }
# print(dic)  # key會去重

