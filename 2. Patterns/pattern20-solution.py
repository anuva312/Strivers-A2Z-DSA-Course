# Pattern to be printed

# Example:

#  Input: 5

#  Output:
#  *        *
#  **      **
#  ***    ***
#  ****  ****
#  **********
#  ****  ****
#  ***    ***
#  **      **
#  *        *

class Solution:
    def printTriangle(self, N):
        for i in range(0,2*N-1):
            for j in range(0,2*N):
                if(i<N):
                    if(j<=i or j>2*N-2-i):
                        print("*",end="")
                    else:
                        print(" ",end="")
                else:
                    k = 2*N-2-i
                    if(j<=k or j>2*N-2-k):
                        print("*",end="")
                    else:
                        print(" ",end="")
            print("\n",end="")

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)