def linear_search(sequence, target):
    """
    線性搜尋或順序搜尋：
        - 時間複雜度：O(n)
        - 介紹：
            是用於在列表中查找目標值的方法。
            它按順序檢查列表中的每個元素的目標值，直到找到匹配或直到搜尋完所有元素。
    """
    for index, item in enumerate(sequence):
        if item == target:
            return index
    return None


if __name__ == "__main__":
    sequence = [1, 3, 5, 9, 15, 44, 75, 99]
    target = 15
    result = linear_search(sequence, target)
    if result is not None:
        print(f"{target} found at position : {result}")
    else:
        print("Not found")
