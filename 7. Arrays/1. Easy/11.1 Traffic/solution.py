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




                
