def topK( nums, k):
    countMap = {}
    for element in nums:
        if element in countMap:
            countMap[element] +=1
        else:
            countMap[element] = 1
    sortedKeys = sorted(list(countMap.keys()),key=lambda x:(countMap[x],x),reverse=True)
    if(len(sortedKeys)<k):
        return sortedKeys
    return sortedKeys[:k]