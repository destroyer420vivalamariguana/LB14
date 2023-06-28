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
    for i in range(n, -1, -1):
        heapify(arr, n, i)

def remove_max_and_heapify(arr):
    # swap first and last element in the list
    arr[0], arr[-1] = arr[-1], arr[0]
    # "remove" last element (max) by ignoring it
    max_element = arr.pop()

    # heapify the root element
    heapify(arr, len(arr), 0)

    return max_element

arr = [10, 5, 3, 4, 1]
max_element = remove_max_and_heapify(arr)
print("Max element removed:", max_element)
print("Heap after removal:", arr)
