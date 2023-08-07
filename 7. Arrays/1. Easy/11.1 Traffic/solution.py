def traffic(n: int, m: int, vehicle: [int]) -> int:
    possible_flips = []
    remaining_flips = m
    max_count = 0
    current_count = 0
    for i in range(n):
        if vehicle[i] == 1:
            current_count +=1
        else:
            possible_flips.append(i)
            if remaining_flips > 0:
                remaining_flips-=1
                current_count+=1
            else:
                if len(possible_flips):
                    next_flip = possible_flips.pop(0)
                    current_count = i-next_flip
                else:
                    current_count = 0
        
        if current_count > max_count:
            max_count = current_count
    return max_count

def trafficAlternative(n: int, m: int, vehicle: [int]) -> int:
    start=0
    max_consecutive_ones = 0
    current_consecutive_ones = 0
    zeroes_count = 0
    end = 0
    while(end<n):
        if(vehicle[end]==0):
            zeroes_count+=1
            if(zeroes_count<=m):
                current_consecutive_ones=end-start+1
            else:
                while (zeroes_count>m):
                    if(start>=end):
                        break
                    if(vehicle[start] == 0):
                        zeroes_count-=1
                    start+=1
                    current_consecutive_ones=end-start+1
        else:
            current_consecutive_ones=end-start+1
        end+=1
        if(current_consecutive_ones>max_consecutive_ones):
            max_consecutive_ones = current_consecutive_ones
    return max_consecutive_ones




                
