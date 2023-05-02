class Solution:
    def printTriangle(self, N):
        count = 1
        for i in range(0,N):
            for j in range(0,N):
                if(j<=i):
                    print(count,end=" ")
                    count=count+1
                else:
                    break;
            print("\n",end="")

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)