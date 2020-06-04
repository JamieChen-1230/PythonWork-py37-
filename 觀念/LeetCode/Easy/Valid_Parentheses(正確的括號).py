class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            '{': '}', '[': ']', '(': ')'
        }
        s = list(s)
        for index, bra in enumerate(s):
            if bra in dic:
                correspond_bra = dic.get(bra)
                if "".join(s).rfind(correspond_bra) != -1:
                    correspond_index = "".join(s).rindex(correspond_bra)
                else:
                    correspond_index = None
                print(correspond_index)
                print(correspond_bra)
                print(s)
                if correspond_index:
                    if (correspond_index-index) % 2 == 1:
                        s.pop(correspond_index)
                        continue
            return False
        return True


ret = Solution().isValid("()()")
print(ret)
