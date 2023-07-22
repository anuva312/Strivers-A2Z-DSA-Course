from typing import List

def pushToEnd(arr: List[int], n: int,i:int, j : int, swapped : bool):
    if(j<n-i-1):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1] = arr[j+1],arr[j]
            swapped = True
        return pushToEnd(arr,n,i,j+1,swapped)  
    return swapped

def bubbleSort(arr: List[int], n: int):
    for i in range(n-1):
        swapped = pushToEnd(arr,n,i,0, False)
        if(swapped == False):
            break