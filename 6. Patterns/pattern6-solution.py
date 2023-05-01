class Solution:
    def printTriangle(self, N):
       for i in range(N,0,-1):
            for j in range(1,i+1):
                print(j,end=" ")
            print("\n",end="")

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)