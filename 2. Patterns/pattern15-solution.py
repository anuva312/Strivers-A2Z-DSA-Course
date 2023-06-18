# Pattern to be printed

# Example:

# Input: 5

# Output:
# ABCDE
# ABCD
# ABC
# AB
# A

import string 

class Solution:
    def printTriangle(self, N):
        alphabets = list(string.ascii_uppercase)
        for i in range(0,N):
            for j in range(0,N):
                if(j<N-i):
                    print(alphabets[j],end="")
                else:
                    break
            print("\n",end="")

    def printTriangleOptimized(self, N):
        for i in range(0,N):
            for j in range(0,N-i):
                print(chr(65+j),end="")
            print()

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangleOptimized(N)