def numberOfWays(n,m,edges):
    countMap = {}
    for element in edges:
        if element in countMap:
            countMap[element] = countMap[element]+1
        else:
            countMap[element] = 1
    for i in range(n):
        if i+1 in countMap:
            edges[i] = countMap[i+1]
        else:
            edges[i] = 0
