import random


def partition(array, start, end, idx_pivot):
    array[start], array[idx_pivot] = array[idx_pivot], array[start]
    pivot = array[start]
    i = start + 1
    j = start + 1
    while j <= end:
        if len(array[j].name) < len(pivot.name):
            array[j], array[i] = array[i], array[j]
            i += 1
        j += 1
    array[start], array[i - 1] = array[i - 1], array[start]
    return i - 1


def quick_sort(array, start, end):
    if end - start < 1:
        return
    pivot = random.randint(start, end)
    i = partition(array, start, end, pivot)
    quick_sort(array, start, i - 1)
    quick_sort(array, i + 1, end)
