def getSecondOrderElements(n,  a):
    largest_element =0
    second_largest_element = 0
    smallest_element = float("inf")
    second_smallest_element = float("inf")

    for element in a:
        if(element > largest_element):
            largest_element = element
        if(element<smallest_element):
            smallest_element = element

    for element in a:
        if(element<largest_element and element>=second_largest_element):
            second_largest_element = element
        if(element>smallest_element and element<=second_smallest_element):
            second_smallest_element  = element
    
    return [second_largest_element,second_smallest_element]


