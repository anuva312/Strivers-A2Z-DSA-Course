# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Auxiliary Space: O(n)

def topK( nums, k):
    countMap = {}
    for element in nums:
        if element in countMap:
            countMap[element] +=1
        else:
            countMap[element] = 1
    sortedKeys = sorted(list(countMap.keys()),key=lambda x:(-countMap[x],-x))
    if(len(sortedKeys)<k):
        return sortedKeys
    return sortedKeys[:k]