def selectionSort(arr):
    length = len(arr) 
    for i in range(0,length):
        minIndex = i
        for j in range(i+1,length):
            if(arr[j]<arr[minIndex]):
                minIndex = j
        if(minIndex != i):
            arr[i],arr[minIndex] = arr[minIndex],arr[i]