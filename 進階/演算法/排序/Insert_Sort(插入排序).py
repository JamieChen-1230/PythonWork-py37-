def insertion_sort(collection):
    """
    插入排序：
        - 時間複雜度：Ο(n^2) ，最好可到Ο(n)
        - 穩定性：穩定
        - 介紹：
            是一種簡單直觀的排序演算法。
            透過建構有序序列，對於未排序數據，在已排序序列中從後向前掃瞄，找到相應位置並插入。
    """
    # 一輪完成一個元素的排序
    for loop_index in range(1, len(collection)):
        insertion_index = loop_index
        print(collection)
        while insertion_index > 0 and collection[insertion_index - 1] > collection[insertion_index]:
            # 交換
            collection[insertion_index], collection[insertion_index - 1] = (
                collection[insertion_index - 1],
                collection[insertion_index],
            )
            insertion_index -= 1

    return collection


if __name__ == "__main__":
    unsorted = [5, 7, 45, 8, 9, 5, 1]
    print(insertion_sort(unsorted))
