def rotateArray(arr, n):
    # in one line using built in functions : arr.append(arr.pop(0))
    first_element = arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1] = first_element
    return arr