"""
Linked-list的資料則散落在記憶體中各處，加入或是刪除元素只需要改變pointer即可完成，
但是相對的，在資料的讀取上比較適合循序的使用，無法直接取得特定順序的值（比如說沒辦法直接知道list[3]）
"""


# 節點
class ListNode:
    def __init__(self, data):
        # 資料內容
        self.data = data
        # 下一個節點位置
        self.next = None


# 單向鏈表
class SingleLinkedList:
    def __init__(self):
        # 鏈表頭
        self.head = None
        # 鏈表當前指標節點
        self.cursor = None

    # 添加節點
    def add_list_item(self, node):
        # 確認node為一節點對象
        if not isinstance(node, ListNode):
            node = ListNode(node)

        # 第一個節點進來時，head和cursor都會指向它
        if self.head is None:
            self.head = node
        else:
            # 第二之後的節點進來後，因為這時cursor還是指向上一個節點，
            # 所以cursor.next能指向新進來的節點(1->2, 2->3, ...)
            self.cursor.next = node
        # 讓指標節點指向至新節點
        self.cursor = node


link = SingleLinkedList()
link.add_list_item(1)
print(link.head.data, link.cursor.data)
link.add_list_item(5)
print(link.head.data, link.cursor.data)
link.add_list_item(10)
print(link.head.data, link.cursor.data)
link.add_list_item(15)
print(link.head.data, link.cursor.data)

print("\n")
cursor = link.head
while cursor:
    print(cursor.data)
    cursor = cursor.next if cursor else None
