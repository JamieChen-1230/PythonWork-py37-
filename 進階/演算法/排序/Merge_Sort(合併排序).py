def merge_sort(collection):
    """
    歸併排序： O(n log n)
        - 時間複雜度：
            拆分：O(n)
            合併：每回合的合併需要花O(n) * 總共需要回合數O(log n) = O(n log n)
            歸併 = 拆分+合併 = O(n) + O(n log n) = O(n log n)
        - 穩定性：穩定
        - 介紹：
            是創建在歸併操作上的一種有效的排序演算法，該演算法是採用分治法的一個非常典型的應用，且各層分治迴歸可以同時進行。
    """
    # 合併
    def merge(left, right):
        result = []
        while left and right:
            # 此相等的話，左邊優先
            result.append((left if left[0] <= right[0] else right).pop(0))
        # 因為採用比較小的先放進去，所以當left或right還有剩的元素時，一定會比result都大
        return result + left + right
    # 終止拆分條件
    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    print(collection)
    # 拆分後合併
    return merge(merge_sort(collection[:mid]), merge_sort(collection[mid:]))


if __name__ == "__main__":
    unsorted = [5, 7, 45, 8, 9, 5, 1]
    print(*merge_sort(unsorted), sep=",")

