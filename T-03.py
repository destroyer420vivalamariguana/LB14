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


def heap_sort(arr):
    n = len(arr)

    # Construir el montículo máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraer elementos uno por uno del montículo
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Intercambiar el elemento máximo con el último elemento no ordenado
        heapify(arr, i, 0)

    return arr


# a. [4, 3, 2, 10, 12, 1, 5, 6, 9, 8]
arr_a = [4, 3, 2, 10, 12, 1, 5, 6, 9, 8]
sorted_arr_a = heap_sort(arr_a)
print("Resultado de Heap Sort en a:", sorted_arr_a)

# b. [10, 20, 15, 30, 40]
arr_b = [10, 20, 15, 30, 40]
sorted_arr_b = heap_sort(arr_b)
print("Resultado de Heap Sort en b:", sorted_arr_b)

# c. [6, 5, 3, 7, 2, 8, -1, -5, 0, 4]
arr_c = [6, 5, 3, 7, 2, 8, -1, -5, 0, 4]
sorted_arr_c = heap_sort(arr_c)
print("Resultado de Heap Sort en c:", sorted_arr_c)
