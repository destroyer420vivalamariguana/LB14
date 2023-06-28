def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def build_max_heap(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


# a. [1, 3, 5, 7, 9]
arr_a = [1, 3, 5, 7, 9]
build_max_heap(arr_a)
print("resultado a:",arr_a)

# b. [9, 7, 5, 3, 1]
arr_b = [9, 7, 5, 3, 1]
build_max_heap(arr_b)
print("resultado b:",arr_b)

# c. [6, 7, 8, 5, 7, 6, 5, 6, 7, 8, 9]
arr_c = [6, 7, 8, 5, 7, 6, 5, 6, 7, 8, 9]
build_max_heap(arr_c)
print("resultado c:",arr_c)
