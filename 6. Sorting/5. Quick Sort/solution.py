def quickSort(arr, startIndex, endIndex):
    if(startIndex>=endIndex):
        return
    pivot = arr[startIndex]
    j = startIndex
    for i in range(startIndex+1, endIndex+1):
        if(arr[i]<=pivot):
            j+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[startIndex],arr[j] = arr[j],arr[startIndex]
    quickSort(arr,startIndex,j-1)
    quickSort(arr,j+1,endIndex)