"""
給定一個整數數組nums和一個目標值target，請你在該數組中找出和為目標值的那兩個整數，並返回他們的數組下標。
(你可以假設每種輸入只會對應一個答案，,但是不能重複利用這個數組中同樣的元素。)
"""
from typing import List


# 爛爆了(自己寫的QQ)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         if len(nums) >= 2:
#             for n1 in nums:
#                 # 同一個值只能使用一次
#                 nums2 = list(nums)
#                 nums2.remove(n1)
#                 for n2 in nums2:
#                     if n1 + n2 == target:
#                         if n1 == n2:
#                             return [nums.index(n1), nums.index(n2, nums.index(n1)+1)]
#                         return [nums.index(n1), nums.index(n2)]
#             return []
#         else:
#             print('num list length must be two or more')
#             return []


# 高手的
# 思路：
#   - 只遍歷一次列表，把遍歷過的元素和下標保存於字典(要把元素值設為key，因為字典裡查找key的速度非常快)
#   - 每次遍歷時，計算出與target之互補值，並去字典找有沒有匹對的
#   - 有匹對的則回傳下標列表；若無則將此元素也加入字典中，並進續下一個迴圈
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        traversed_nums = {}
        # enumerate() 會返回元素的下標和值
        for id, n in enumerate(nums):
            # 互補值
            difference = target - n
            if difference in traversed_nums:  # 判斷之前此互補值是否有出現過
                return [traversed_nums[difference], id]
            # 元素值設為key，下標設為value
            traversed_nums.setdefault(n, id)


ret = Solution().twoSum([3, 3], 6)
print(ret)

