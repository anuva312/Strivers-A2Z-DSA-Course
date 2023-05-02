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

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)