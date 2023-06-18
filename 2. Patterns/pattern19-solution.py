# Pattern to be printed

# Example:

# Input: 5

# Output:

# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********

class Solution:
    def printTriangle(self, N):
        for i in range(0,2*N):
            for j in range(0,2*N):
                if(i<N):
                    if(j not in range(N-i,N+i)):
                        print("*",end="")
                    else:
                        print(" ",end="")
                else:
                    k = 2*N-1-i
                    if(j not in range(N-k,N+k)):
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