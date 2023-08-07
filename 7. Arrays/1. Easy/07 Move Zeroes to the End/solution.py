def moveZeros(n: int,  a: [int]) -> [int]:
    zero_position = -1
    for i in range(n):
        if a[i] == 0:
            if zero_position == -1:
                zero_position = i
        elif zero_position>-1:
            a[i],a[zero_position] = a[zero_position],a[i]
            if (zero_position+1) < n and (zero_position+1)<=i and a[zero_position+1]==0:
                zero_position+=1
    return a
            
