class Solution:
    def printSquare(self, N):
        for _ in range(N):
            for _ in range(N):
                print("*",end=" ")
            print("\n",end="")


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printSquare(N)