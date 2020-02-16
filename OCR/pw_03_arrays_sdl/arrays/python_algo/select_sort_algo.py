select_sort(array, len):
    for i in range(len):
        # find min index in array between i and len
        min = array_min(array[i:len])
        swap(array[i], array[min])
