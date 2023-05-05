class Solution:
    def printTriangle(self, N):
        for i in range (0,2*N-1):
            if(i < N):
                row = i
            else:
                row = 2*N-2-i
            value = N
            count = row
            for j in range(1,2*N):
                print(value,end=" ")
                if(value > 0 and count>0):
                    value = value-1
                    count = count-1
                elif(j>=2*N-1-row and count == 0):
                    value = value+1
            print("\n",end="")

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)