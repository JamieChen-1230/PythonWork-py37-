"""
給出一個32位的有符號整數，將這個整數中每位上的數字進行反轉。
反轉的數需在[-2^31, 2^31-1]範圍中，否則返回0。
"""


# 自己寫的(OK)
# class Solution:
#     def reverse(self, x: int) -> int:
#         minus = None
#         # 轉為list
#         x_list = list(str(x))
#         if x_list[0] == '-':
#             minus = x_list.pop(0)
#         # 反轉list
#         x_list = list(reversed(x_list))
#         if minus:
#             x_list.insert(0, minus)
#         # 先轉為字符串再轉為整數
#         x = int("".join(x_list))
#         return x if (-2 ** 31 < x < 2 ** 31 - 1) else 0


# 別人寫的(更為簡潔)
class Solution(object):
    def reverse(self, x):
        minus = 1
        if x < 0:
            minus = -1
        # 透過字符串反轉
        x = str(abs(x))[::-1]
        x = int(x)*minus
        return x if (-2**31 < x < 2**31-1) else 0


ret = Solution().reverse(-1234567893)
print(ret)

