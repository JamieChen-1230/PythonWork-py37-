def quick_sort(collection):
    """
    快速排序法：
        - 時間複雜度：Ο(n log n)
        - 穩定性：不穩定
        - 介紹：
            是先在序列中找出一個元素作為支點(pivot)，然後想辦法將比支點的元素移動到支點元素的左邊，比支點大的元素移動到支點元素的右邊，
            接著再用同樣的方法繼續對支點的左邊子陣列和右邊子陣列進行排序。
    """
    length = len(collection)
    if length <= 1:
        return collection
    else:
        # 使用最後一個元素作為支點
        pivot = collection.pop()
        # 以支點為分界，分出大小兩個陣列
        greater, lesser = [], []
        for element in collection:
            if element > pivot:
                greater.append(element)
            else:
                lesser.append(element)
        # 以找到支點位置，而大小兩個陣列繼續做遞歸
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    unsorted = [5, 7, 45, 8, 9, 5, 1]
    print(quick_sort(unsorted))
