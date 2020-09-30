from typing import List

array = [int(x) for x in input().split()]

def selection(array: List, lo: int, hi: int) -> None:
    i = lo

    while i < hi:
        j = i
        _min = j
        while j < hi:
            if array[j] < array[_min]:
                _min = j
            j += 1
        array[_min], array[i] = array[i], array[_min]
        i += 1


selection(array, 0, len(array))
print(array)