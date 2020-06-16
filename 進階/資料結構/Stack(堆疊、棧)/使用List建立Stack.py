"""
Stack(堆疊、棧)：
    是一種概念性的抽象資料結構，具有「後進先出」的特性，其中添加或刪除都發生在同一端，這一端被稱為「棧頂」，與其對應的叫「棧底」。
"""


class Stack:
    def __init__(self):
        """用List實作，串列尾為棧頂"""
        self.items = []

    def isEmpty(self):
        """測試棧是否為空(不需要參數，返回布林值)"""
        return self.items == []

    def clear(self):
        """清空棧(沒有返回值)"""
        self.items.clear()

    def push(self, element):
        """將一個新項添加到棧的頂部"""
        self.items.append(element)

    def pop(self):
        """從棧中刪除並返回頂部項"""
        if self.isEmpty():
            return False, "目前為空棧"
        return self.items.pop()

    def top(self):
        """從棧中返回頂部項(不會刪除)"""
        if self.isEmpty():
            return False, "目前為空棧"
        return self.items[-1]

    def size(self):
        """返回棧中的元素數量"""
        return len(self.items)


s = Stack()
print(s.top())  # => (False, '目前為空棧')
print(s.pop())  # => (False, '目前為空棧')
s.push('A')
s.push('B')
s.push('C')
print(s.isEmpty())  # => False
print(s.size())  # => 3
print(s.top())  # => C
print(s.pop())  # => C
print(s.size())  # => 2
s.clear()
print(s.isEmpty())  # => True



