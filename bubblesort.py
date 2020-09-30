from typing import List

array = [int(x) for x in input().split()]

def bubblesort(array: List, lo: int, hi: int) -> None:
    for i in range(lo, hi):
        for j in range(lo, hi - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

bubblesort(array, 0, len(array))
print(array)