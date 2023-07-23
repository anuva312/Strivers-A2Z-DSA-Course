def getFrequencies(v) : 
    frequency_count = {}
    highest_frequency_elements = []
    lowest_frequency_elements = []
    if(len(v) == 0):
        return [0,0]
    for element in v:
        if element in frequency_count:
            frequency_count[element] += 1
        else:
            frequency_count[element] = 1
    lowest_frequency = highest_frequency = frequency_count[v[0]]

    for element in v:
        new_frequency = frequency_count[element]
        if(new_frequency>highest_frequency):
            highest_frequency = new_frequency
            highest_frequency_elements= [element]
        elif new_frequency == highest_frequency:
            highest_frequency_elements.append(element)
        if(new_frequency<lowest_frequency):
            lowest_frequency = new_frequency
            lowest_frequency_elements= [element]
        elif new_frequency == lowest_frequency:
            lowest_frequency_elements.append(element)
    return [min(highest_frequency_elements),min(lowest_frequency_elements)]