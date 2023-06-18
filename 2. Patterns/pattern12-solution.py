# Pattern to be printed

# Example:

# Input: 5

# Output:
# 1                 1
# 1 2             2 1
# 1 2 3         3 2 1
# 1 2 3 4     4 3 2 1
# 1 2 3 4 5 5 4 3 2 1

class Solution:
    def printTriangle(self, N):
        for i in range(0,N):
            for j in range(0,2*N):
                if(j<=i):
                    print(j+1,end = " ")
                elif(j>=(2*N-i-1)):
                    print(2*N-j,end=" ")
                else:
                    print(" ",end=" ")
            print("\n",end="")

    def printTriangleAlternative(self,N):
        spaces = 2*N-2
        for i in range(1,N+1):
            for j in range(1,i+1):
                print(j,end=" ")
            for _ in range(spaces):
                print(" ",end=" ")
            for j in range(i,0,-1):
                print(j,end=" ")
            spaces=spaces-2
            print("\n",end="")

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)