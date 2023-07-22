def mergeSort(arr, l, r):
    if(l >= r):
        return
    m = (r-l)//2
    mergeSort(arr,l,l+m)
    mergeSort(arr,l+m+1,r)
    k=l
    i=j=0
    arr1 = arr[l:l+m+1]
    arr2 =arr[l+m+1:r+1]
    while(i<len(arr1) and j<len(arr2)):
        if(arr1[i]<=arr2[j]):
            arr[k] = arr1[i]
            i+=1
        else:
            arr[k] = arr2[j]
            j+=1
        k+=1
    while(i<len(arr1)):
        arr[k] = arr1[i]
        i+=1
        k+=1
    while(j<len(arr2)):
        arr[k] = arr2[j]
        j+=1
        k+=1
    print(arr)
    