def heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] > arr[left]:
        smallest = left

    if right < n and arr[smallest] > arr[right]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)


# a. [9, 7, 5, 3, 1]
arr_a = [9, 7, 5, 3, 1]
n_a = len(arr_a)

for i in range(n_a // 2 - 1, -1, -1):
    heapify(arr_a, n_a, i)

print("Resultado de Heapify en a:", arr_a)

# b. [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
arr_b = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
n_b = len(arr_b)

for i in range(n_b // 2 - 1, -1, -1):
    heapify(arr_b, n_b, i)

print("Resultado de Heapify en b:", arr_b)
