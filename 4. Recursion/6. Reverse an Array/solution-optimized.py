# Time Complexity : O(N)
# Space Complexity : O(N)
# Auxilary Space Used : O(1)

def inPlaceReversing(arr,start,end):
    if(start>=end):
        return
    arr[start], arr[end] = arr[end], arr[start]
    inPlaceReversing(arr,start+1,end-1)

def reverseArray(n, nums):
    inPlaceReversing(nums,0,n-1)
    return nums