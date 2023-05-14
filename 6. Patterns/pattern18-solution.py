# Pattern to be printed

# Example:

# Input: 5

# Output:
# E
# E D
# E D C
# E D C B
# E D C B A

import string 

class Solution:
    def printTriangle(self, N):
        alphabets = list(string.ascii_uppercase)
        for i in range(0,N):
            for j in range(0,i+1):
                print(alphabets[N-1-j],end=" ")
            print("\n",end="")

    def printTriangleOptimized(self, N):
        for i in range(0,N):
            for j in range(0,i+1):
                print(chr(65+N-1-j),end=" ")
            print()

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangleOptimized(N)