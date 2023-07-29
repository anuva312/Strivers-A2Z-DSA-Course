# Time Complexity: O(N)
# Space Complexity: O(N) (due to the call stack)
# Auxiliary Space: O(1)

class Solution:
    def printNos(self, n):
        if n >= 1:
            print(n, end=" ")
            self.printNos(n - 1)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printNos(N)
        print()
