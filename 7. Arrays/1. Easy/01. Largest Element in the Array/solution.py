def largestElement(arr, n) :
    largest_element = 0
    for element in arr:
        if element > largest_element:
            largest_element =element
    return largest_element


