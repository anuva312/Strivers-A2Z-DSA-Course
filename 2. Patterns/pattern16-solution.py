# Pattern to be printed

# Example:

# Input: 5

# Output:
# A
# BB
# CCC
# DDDD
# EEEEE

import string 

class Solution:
    def printTriangle(self, N):
        alphabets = list(string.ascii_uppercase)
        for i in range(0,N):
            for j in range(0,N):
                if(j<=i):
                    print(alphabets[i],end="")
                else:
                    break
            print("\n",end="")

    def printTriangleOptimized(self, N):
        for i in range(0,N):
            for _ in range(0,i+1):
                print(chr(65+i),end="")
            print("\n",end="")

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangleOptimized(N)