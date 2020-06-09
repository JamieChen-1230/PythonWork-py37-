"""
將兩個有序鏈表合併為一個新的有序鏈表並返回，新鏈表是通過拼接給定的兩個鏈表的所有節點。
"""
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 自己寫的(略差)
class Solution_ByMe:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 先設定一個虛假起始點
        dummy_node = ListNode(0)
        # 指標
        cursor = dummy_node
        while l1 or l2:
            # 如果沒值了就設為無窮大，以便後面判斷
            l1_val = l1.val if l1 else math.inf
            l2_val = l2.val if l2 else math.inf
            if l1_val <= l2_val:
                cursor.next = l1
                l1 = l1.next
            else:
                cursor.next = l2
                l2 = l2.next
            # 指標指到下一個節點
            cursor = cursor.next
        return dummy_node.next


# 高手寫的(較快)
# 思路：
#   - 前面一樣是兩兩比較
#   - 但當有一鏈表完結時，直接跳出迴圈，並把剩下的鏈表接上
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 設定一個虛假起始點和指標
        dummy_node = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            print(cur.val)
        # 指向l1或l2剩下的鏈表
        cur.next = l1 or l2  # 通過or篩選出有值的鏈表
        return dummy_node.next


l1 = ListNode(2, ListNode(10, ListNode(11)))
l2 = ListNode(5, ListNode(6))
ret = Solution().mergeTwoLists(l1, l2)
while ret:
    print(ret.val)
    ret = ret.next if ret else None
