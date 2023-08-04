def sortedArray(a: [int], b: [int]) -> [int]:
    first_array_position = 0
    second_array_position = 0
    first_array_size = len(a)
    second_array_size = len(b)
    combined_array = [] 
    
    while(first_array_position < first_array_size and second_array_position < second_array_size):
            if a[first_array_position]==b[second_array_position]:
                next_element = a[first_array_position]
                first_array_position+=1
                second_array_position+=1
            elif a[first_array_position]<b[second_array_position]:
                next_element = a[first_array_position]
                first_array_position+=1
            else:
                next_element = b[second_array_position]
                second_array_position+=1 
            
            if len(combined_array):
                if next_element != combined_array[-1]:
                    combined_array.append(next_element)
            else:
                combined_array.append(next_element)


    while(first_array_position < first_array_size):
        if(a[first_array_position] != combined_array[-1]):
            combined_array.append(a[first_array_position])
        first_array_position+=1

    while(second_array_position < second_array_size):
        if(b[second_array_position] != combined_array[-1]):
            combined_array.append(b[second_array_position])
        second_array_position+=1
       
    return combined_array