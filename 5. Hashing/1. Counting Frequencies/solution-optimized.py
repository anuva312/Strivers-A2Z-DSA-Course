# Time Complexity: O(N)
# Space Complexity: O(1)
# Auxiliary Space: O(1)

def frequencyCount(arr,N,P):
    i=0
    while i < N:
        if(arr[i] <0 or arr[i]>N or arr[i]>P):
            i+=1
            continue
        element_index = arr[i]-1
        if(arr[element_index]>0):
            arr[i] = arr[element_index]
            arr[element_index] = -1
        else:
            arr[element_index]-=1
            arr[i]=0
            i+=1
    for i in range(N):
        if(arr[i]<0):
            arr[i]*=-1
        else:
            arr[i]=0