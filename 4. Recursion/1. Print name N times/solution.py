# Time Complexity: O(n)
# Space Complexity: O(n) (due to the call stack)
# Auxiliary Space: O(1)


class Solution:
    def printGfg(self, n):
        if n > 0:
            print("GFG", end=" ")
            self.printGfg(n - 1)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printGfg(N)
        print()
