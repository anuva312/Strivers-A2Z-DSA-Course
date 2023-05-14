# Pattern to be printed

# Example:

# Input: 5

# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

class Solution:
    def printTriangle(self, N):
        count = 1
        for i in range(0,N):
            for j in range(0,N):
                if(j<=i):
                    print(count,end=" ")
                    count=count+1
                else:
                    break
            print("\n",end="")

    def printTriangleRefactored(self, N):
        count = 1
        for i in range(0,N):
            for _ in range(0,i+1):
                print(count,end=" ")
                count=count+1
            print("\n",end="")

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangleRefactored(N)