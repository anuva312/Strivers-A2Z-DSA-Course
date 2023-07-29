# For Optimized :
#   Time Complexity : O(1)
#   Space Complexity : O(1)

# For Brute Force :
#   Time Complexity : O(N)
#   Space Complexity : O(N)

class Solution:
    def sumOfSeries(self, N):
        if N < 0:
            return 0
        return N**3 + self.sumOfSeries(N - 1)

    def sumOfSeriesOptimized(self, N):
        # Note : S = [n^2 *(n + 1)^2]/4, where S is the sum of cubes and n is the number of natural numbers taken
        return (N**2 * (N + 1) ** 2) // 4


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        print(ob.sumOfSeries(N))

