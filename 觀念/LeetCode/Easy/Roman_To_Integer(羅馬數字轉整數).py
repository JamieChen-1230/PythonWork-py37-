"""
將羅馬數字轉為整數。
特殊情形：
    I可以放在V (5)和X (10)的左邊，來表示4和9。
    X可以放在L (50)和C (100)的左邊，來表示40和90。
    C可以放在D (500)和M (1000)的左邊，來表示400和900。
"""


# 自己寫的(u秀)
class Solution:
    def romanToInt(self, s: str) -> int:
        ROMAN_dic = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }
        sum = 0
        prei_num = 0
        # 字串從尾到頭遍歷
        for i in s.upper()[::-1]:
            i_num = ROMAN_dic.get(i, 0)
            # 當後面的值比前面的值大時，表示遇到特殊情形，要加負號
            minus = -1 if prei_num > i_num else 1
            sum += i_num * minus
            # 保存前一個值用於比較
            prei_num = i_num
        return sum


ret = Solution().romanToInt("VII")
print(ret)

ret = Solution().romanToInt("IV")
print(ret)

