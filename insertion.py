from typing import List

array = [int(x) for x in input().split()]

def insertion(array: List, lo: int, hi: int) -> None:
    i = lo
    while i < hi:
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
        i += 1


insertion(array, 0, len(array))
print(array)