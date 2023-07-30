# Time Complexity: O(n)
# Space Complexity: O(m)
# Auxiliary Space: O(m)

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

            
# Time Complexity: O(N)
# Space Complexity: O(N)
# Auxiliary Space: O(N)

def frequencyCount(arr, N, P):
    frequency_count = []
    for i in range(N):
        frequency_count.append(0)
    for element in arr:
        if(element <= N):
            frequency_count[element-1]+=1
    for i in range(N):
        arr[i] = frequency_count[i]


