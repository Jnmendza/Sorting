# Initial Commit
# TO-DO: Complete the selection_sort() function below
arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        for n in range(smallest_index + 1, len(arr)):
            # (hint, can do in 3 loc)
            # TO-DO: swap
            if arr[n] < arr[smallest_index]:
                (arr[n], arr[smallest_index]) = (arr[smallest_index], arr[n])
                print("selection", arr)

    return arr


# # TO-DO:  implement the Bubble Sort function below
# arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

def bubble_sort( arr ):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1):
            current_index = j
            next_index = current_index + 1
            print("curr idx", current_index)
            print("nxt idx", next_index)
            if arr[current_index] > arr[next_index]:
                (arr[current_index], arr[next_index]) = (arr[next_index], arr[current_index])
                print("bubble if arr", arr)
            elif arr[current_index] < arr[next_index]:
                print("bubble else arr", arr)
                pass

    return arr


# selection_sort(arr)
bubble_sort(arr)
print(arr)
