# Brute Force Approach
def majorityElement(v):
    countMap = {}
    for element in v:
        if element in countMap:
            countMap[element] += 1
        else:
            countMap[element] = 1
    maxCount = len(v) // 2 + 1
    for count in countMap:
        if countMap[count] >= maxCount:
            return count
    return -1
