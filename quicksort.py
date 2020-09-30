from typing import List

array = [int(x) for x in input().split()]

def quicksort(array: List, lo: int, hi: int) -> None:
    if lo < hi:
        pivot = partition(array, lo, hi)

        quicksort(array, lo, pivot)
        quicksort(array, pivot + 1, hi)


def partition(array: List, lo: int, hi: int) -> int:
    i, j = lo - 1, lo
    pivot = hi - 1

    while j < pivot:
        if array[j] < array[pivot]:
            i += 1
            array[i], array[j] = array[j], array[i]
        j += 1
    i += 1

    array[i], array[pivot] = array[pivot], array[i]

    return i


quicksort(array, 0, len(array))
print(array)