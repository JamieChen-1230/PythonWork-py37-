def bubble_sort(collection):
    """
    泡沫排序：Ο(n^2)  【BEST可到Ο(n)】
    有時也被稱做沉降排序，是一種比較簡單的排序演算法。
    透過遍歷要排序的列表，把相鄰兩個不符合排列規則的數據項交換位置，然後重複遍歷列表，直到不再出現需要交換的數據項。
    """
    length = len(collection)
    # 因為從最後一位到第一位也只要(length - 1)次
    for i in range(length - 1):
        swapped = False
        print(collection)
        for j in range(length - 1 - i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swapped:
            break
    return collection


if __name__ == "__main__":
    unsorted = [5, 7, 45, 8, 9, 5, 1]
    print('Ans:', bubble_sort(unsorted))
