def selection_sort(collection):
    """
    選擇排序：Ο(n^2) 【BEST還是Ο(n^2)】
    是一種簡單直觀的排序演算法。
    首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然後，再從剩餘未排序元素中繼續尋找最小（大）元素，然後放到已排序序列的末尾。
    """

    length = len(collection)
    for i in range(length - 1):
        least = i
        print(collection)
        for k in range(i + 1, length):
            if collection[k] < collection[least]:
                least = k
        if least != i:
            collection[least], collection[i] = (collection[i], collection[least])
    return collection


if __name__ == "__main__":
    unsorted = [5, 7, 45, 8, 9, 5, 1]
    print(selection_sort(unsorted))
