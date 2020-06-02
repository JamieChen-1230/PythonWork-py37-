# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 高手寫的
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 先設定一個虛假起始點
        dummy_node = ListNode(0)
        # 指標
        cursor = dummy_node
        # 進位
        carry = 0
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            sum = num1 + num2 + carry

            carry = sum // 10  # 計算進位值
            cursor.next = ListNode(sum % 10)  # 餘數
            cursor = cursor.next  # 指標指到下一個節點
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        # 如果最後一位數還有進位值的話，也要為它創造一個節點
        if carry:
            cursor.next = ListNode(carry)
        # dummy_node是我們創來當起始值的假節點，dummy_node.next開始才是真正的答案
        return dummy_node.next


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
ret = Solution().addTwoNumbers(l1, l2)
while ret:
    print(ret.val)
    ret = ret.next if ret else None
