def binary_search(sequence, target):
    """
    二分搜尋法：O(log n)
    用於查尋已排序數組中目標值的位置。
    它將目標值與數組的中間元素進行比較，如果它們不相等，則目標的一半被消除，並且在剩下的一半上繼續搜尋直到成功。
    """
    # 設置選取範圍的指標
    low = 0
    upper = len(sequence) - 1
    while low <= upper:
        mid = (low + upper) // 2  # 取中間索引的值
        if sequence[mid] < target:    # 若搜尋值比中間的值大，取右半
            low = mid + 1
        elif sequence[mid] > target:  # 若搜尋值比中間的值小，取左半
            upper = mid - 1
        else:  # 若搜尋值等於中間的值，則回傳
            return mid
    return None


sequence = [1, 3, 5, 9, 15, 44, 75, 99]
target = 44
result = binary_search(sequence, target)
if result is not None:
    print(f"{target} found at position : {result}")
else:
    print("Not found")
