"""
檢測Integer是否回文，不能使用字符串。
"""


# 自己寫的(普普)
class Solution_ByMe:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x_list = []
            while x:
                x, remainder = divmod(x, 10)
                x_list.append(remainder)
            return x_list == list(reversed(x_list))


# 別人寫的(快一點點)
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         return self.reverse(x) == x
#
#     def reverse(self, n):
#         rev, rem = 0, abs(n)
#         while rem:
#             rev = rev * 10 + rem % 10
#             rem //= 10
#         return rev


# 不合規定(用了字串)，但很快
class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        return x == x[::-1]


ret = Solution().isPalindrome(121)
print(ret)
