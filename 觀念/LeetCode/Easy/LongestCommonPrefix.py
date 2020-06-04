from typing import List


# 自己寫的(普普)
class Solution_ByMe:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index = 1
        dic = {}
        return self.findprefix(strs, dic, index, '')

    def findprefix(self, strs, dic, index, ans):
        for word in strs:
            s = word[0:index]
            if not s:
                break
            if index > len(word):
                break
            # 透過字典存前綴和出現次數
            if s not in dic:
                dic.setdefault(s, 1)
            else:
                dic[s] += 1
        for k, val in dic.items():
            # 若前綴的出現次數少於題目長度，表示至少有一個元素沒有共同前綴
            if val == len(strs):
                ans = k
                dic.pop(k)  # 刪除舊值，不然有能會造成無窮遞歸
                return self.findprefix(strs, dic, index+1, ans)
        return ans


# 高手的
class Solution:
    def longestCommonPrefix(self, strs):
        prefix = ""
        if len(strs) == 0:
            return prefix

        for i in range(len(min(strs))):  # 跑最少的次數
            sample = strs[0][i]
            # all(全部為True)才為True
            if all(a[i] == sample for a in strs):
                prefix += sample
            else:
                break
        return prefix


# 高手的特殊思路(使用排序)
class Solution_sp:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 極端情況判斷
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        # 透過排序機制，讓差異最大兩者(頭尾元素)進行比較即可
        strs.sort()
        ans = ""
        # 透過zip拆分成一個個元組(x, y)，再使用元組拆包x,y=(x, y)
        for x, y in zip(strs[0], strs[-1]):
            if x == y:
                ans += x
            else:
                break
        return ans


ret = Solution().longestCommonPrefix(["a"])
print(ret)

