# Pattern to be printed

# Example:

# Input: 4

# Output:
# ****
# *  *
# *  *
# ****

class Solution:
    def printTriangle(self, N):
        for i in range(0,N):
            for j in range(0,N):
                if(i==N-1 or i==0):
                    print("*",end="")
                else:
                    if(j==0 or j==N-1):
                        print("*",end="")
                    else:
                        print(" ",end="")
            print("\n",end="")

    def printTriangleRefactored(self, N):
        for i in range(N):
            for j in range(N):
                if i == 0 or i == N-1 or j == 0 or j == N-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangleRefactored(N)