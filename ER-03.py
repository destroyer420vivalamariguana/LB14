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

def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    build_max_heap(arr)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
heap_sort(arr)
print("Sorted array is", arr)
