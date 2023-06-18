# Pattern to be printed

# Example:

# Input: 5

# Output:
# A
# AB
# ABC
# ABCD
# ABCDE

import string 

class Solution:
    def printTriangle(self, N):
        alphabets = list(string.ascii_uppercase)
        for i in range(0,N):
            for j in range(0,i+1):
                print(alphabets[j],end="")
            print("\n",end="")

    def printTriangleOptimized(self,N):
        for i in range(1, N+1):
            for j in range(65, 65+i):
                print(chr(j), end="")
            print()

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangleOptimized(N)