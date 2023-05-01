class Solution:
    def printTriangle(self, N):
        for i in range(1,2*N):
            for j in range(0,2*i):
                if(i<=N):
                    if(j%2 != 0):
                        print("*",end=" ")
                else:
                    if(j<=2*(2*N-i)):
                        if(j%2 != 0):
                            print("*",end=" ")
            print("\n",end="")

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)