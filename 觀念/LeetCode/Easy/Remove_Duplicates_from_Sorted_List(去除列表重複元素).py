"""
給定一個排序數組，你需要在原地刪除重複出現的元素，使得每個元素只出現一次，返回移除後數組的新長度。
不要使用額外的數組空間，你必須在原地修改輸入數組並在使用O(1)額外空間的條件下完成。
範例：
    給定nums = [0,0,1,1,1,2,2,3,3,4]，
    函數應該返回新的長度5，並且原數組nums的前五個元素被修改為0, 1, 2, 3, 4。
    你不需要考慮數組中超出新長度後面的元素。
"""
from typing import List


# 高手寫的
# 思路(雙指針法)：
#    - 初始時，後指針為0，前指針為1
#    - 當前指針和後指針指向的數字相等，前指針向前一步
#    - 當前指針和後指針指向的數字不同，後指針向前一步，把前指針指向的數字賦給後指針指向的位置
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1


ret = Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(ret)
