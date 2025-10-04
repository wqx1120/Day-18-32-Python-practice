def bubble_sort(arr): 
    #compare neighbors, change the position if left one is larger
    #O(n^2)
    #O(1)
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr



def quicksort(arr):
    # pick a pivot, move smaller onee to the left, larger ones to the left
    # O(nlogn), but O(n^2) in worst case
    # O(logn)
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

