def bin_search(array, left, right, x):
    if left == right:
        return right
    mid = left + (right - left) / 2
    if array[mid] == x:
        return mid
    if x < array[mid]:
        return bin_search(array, left, mid, x)
    else:
        return bin_search(array, mid + 1, right, x)
