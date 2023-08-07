def isSorted(n,a):
    is_sorted = 1
    if(len(a)>1):
        for i in range(1,n):
            prev_index = i-1
            if(a[prev_index]>a[i]):
                is_sorted = 0
                break
    return is_sorted