# Pattern to be printed

# Example:

# Input: 5

# Output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            for _ in range(1,i+1):
                print(i,end=" ")
            print("\n",end="")

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)