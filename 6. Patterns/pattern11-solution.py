# Pattern to be printed

# Example:

# Input: 5

# Output:
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1

class Solution:
    def printTriangle(self, N):
       for i in range(0,N):
            for j in range(0,i+1):
                if(j<i+1):
                    if(i%2 == 0):
                        if(j%2==0):
                            print("1",end=" ")
                        else:
                            print("0",end=" ")
                    else:
                        if(j%2==0):
                            print("0",end=" ")
                        else:
                            print("1",end=" ")
            print("\n",end="")

    def printTriangleRefactored(self,N):
        for i in range(0,N):
            start = 1 if i%2 == 0 else 0
            for _ in range(0,i+1):
                print(start,end=" ")
                start = 1-start
            print("\n",end="")

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangleRefactored(N)