class Solution:
    def printTriangle(self, N):
        for i in range(0,N):
            for j in range(1,2*N):
                if(j in range(N-i,N+i+1)):
                    print("*",end="")
                elif(j<N-i):
                    print(" ",end="")
                else:
                    print("",end="")
            print("\n",end="")

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)