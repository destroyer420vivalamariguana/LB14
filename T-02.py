def percolate_down(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        percolate_down(arr, n, largest)

def delete_max(arr):
    n = len(arr)
    if n == 0:
        return None

    max_val = arr[0]
    arr[0] = arr[n - 1]
    arr.pop()

    percolate_down(arr, n - 1, 0)

    return max_val

# a. [9, 7, 8, 3, 1]
arr_a = [9, 7, 8, 3, 1]
max_val_a = delete_max(arr_a)
print("Elemento máximo eliminado en a:", max_val_a)
print("Resultado después de Percolate Down en a:", arr_a)

# b. [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
arr_b = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
max_val_b = delete_max(arr_b)
print("Elemento máximo eliminado en b:", max_val_b)
print("Resultado después de Percolate Down en b:", arr_b)