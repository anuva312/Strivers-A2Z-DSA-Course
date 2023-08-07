def getSingleElement(arr):
    array_length = len(arr)
    for i in range(0,array_length,2):
        if(i==array_length-1 or arr[i]!=arr[i+1]):
            return arr[i]