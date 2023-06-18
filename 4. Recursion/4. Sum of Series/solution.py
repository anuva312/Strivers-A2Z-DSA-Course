# User function Template for python3


class Solution:
    def sumOfSeries(self, N):
        if N < 0:
            return 0
        return N**3 + self.sumOfSeries(N - 1)

    def sumOfSeriesOptimized(self, N):
        return (N**2 * (N + 1) ** 2) // 4


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        print(ob.sumOfSeries(N))
# } Driver Code Ends
