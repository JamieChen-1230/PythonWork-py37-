"""
給定一個只包括'('',   ')',  '{',   '}',  '[', '  ]' 的字符串，判斷字符串是否有效。
有效字符串需滿足：
    左括號必須用相同類型的右括號閉合。
    左括號必須以正確的順序閉合。
    注意：空字符串可被認為是有效字符串。
"""


# 高手寫的(效率不高，但思路很特殊，雖然有點投機取巧)
# 思路：
#   - 因為題目只會給() [] {}，並沒有包括其他元素，EX:{4}之類的，
#   - 所以題目最內層一定會是這() [] {}三種形式，
#   - 故只要循環替代掉即可
class Solution_sp:
    def isValid(self, s: str) -> bool:
        while '()' in s or '[]' in s or '{}' in s:
            # print(s)
            s = s.replace('()', '')
            # print(s)
            s = s.replace('[]', '')
            # print(s)
            s = s.replace('{}', '')
        return s == ''


# 高手寫的(666666)
# 思路：
#   - 最後入棧的左括號，一定會先遇到它對應的右括號
class Solution(object):
    def isValid(self, s):
        dic = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in s:
            print(stack)
            if c in dic:
                # 將左括號加入棧中
                stack.append(c)
            else:  # 右括號
                if stack:
                    last_c = stack.pop()
                    if c != dic[last_c]:
                        return False
                else:
                    return False
        return not stack


ret = Solution().isValid('({([])}[])()')
print(ret)

# ret = Solution_sp().isValid('({()})()')
# print(ret)

