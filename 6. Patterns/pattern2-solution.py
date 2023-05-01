class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            for _ in range(i):
                print("*",end=" ")
            print("\n",end="")

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)