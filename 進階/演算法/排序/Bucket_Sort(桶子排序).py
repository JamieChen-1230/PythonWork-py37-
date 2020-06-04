DEFAULT_BUCKET_SIZE = 5


def bucket_sort(my_list, bucket_size=DEFAULT_BUCKET_SIZE):
    """
    桶排序或所謂的箱排序：
        - 介紹：
            是一個排序演算法 ，工作的原理是將數組分到有限數量的桶子裡。
            每個桶子再個別排序，有可能再使用別的排序演算法或是以迴歸方式繼續使用桶排序進行排序。
            (通常會以插入排序等適合少量資料的演算法進行排序之後，再依照桶子的順序把桶子中的元素串接在一起)
    """
    min_value, max_value = (min(my_list), max(my_list))
    # 計算桶子最大數量
    bucket_count = (max_value - min_value) // bucket_size + 1
    # 生成桶子
    buckets = [[] for _ in range(int(bucket_count))]

    for i in range(len(my_list)):
        # 分配數值到桶子中(越相近的數值會被分配到一起，越大的數值也會被分配到較後面的桶子)
        buckets[int((my_list[i] - min_value) // bucket_size)].append(my_list[i])
    # print(buckets)
    # print([buckets[i][j] for i in range(len(buckets)) for j in range(len(buckets[i]))])

    return sorted(
        [buckets[i][j] for i in range(len(buckets)) for j in range(len(buckets[i]))]
    )


if __name__ == "__main__":
    unsorted = [5, 7, 45, 15, 9, 5, 1]
    print(bucket_sort(unsorted))
