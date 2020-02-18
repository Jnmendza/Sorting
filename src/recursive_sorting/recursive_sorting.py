# TO-DO: complete the helper function below to merge 2 sorted arrays


TestA = [0, 1, 2, 4, 6, 7, 8, 9]
TestB = [0, 1, 3, 5, 7, 8]
TestArr = [5, 1, 7, 0, 3, 8]


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    arrA.extend(arrB)

    for i in range(len(merged_arr)):
        merged_arr[i] = arrA[i]

    merged_arr.sort()
    print(merged_arr)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    split = len(arr) // 2
    left = arr[:split]
    right = arr[split:]

    return merge(merge_sort(left), merge_sort(right))



# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO
#
#     return arr
#
#
# def merge_sort_in_place(arr, l, r):
#     # TO-DO
#
#     return arr

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timesort( arr ):
#
#     return arr

merge(TestA, TestB)

merge_sort(TestArr)
