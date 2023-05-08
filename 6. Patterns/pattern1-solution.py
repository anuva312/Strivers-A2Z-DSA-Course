# Pattern to be printed

# Example:

# Input: 5

# Output:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *


class Solution:
    def printSquare(self, N):
        for _ in range(N):
            for _ in range(N):
                print("*",end=" ")
            print("\n",end="")

    def printSquareOptimized(self,N):
        pattern = ""
        for _ in range(N):
            pattern += "* "
        for _ in range(N):
            print(pattern)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printSquareOptimized(N)