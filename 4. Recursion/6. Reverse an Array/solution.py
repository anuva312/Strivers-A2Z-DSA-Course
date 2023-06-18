class Solution:
    def __init__(self):
        self.reversed_array = []

    def getReversedArray(self):
        return self.reversed_array

    def createReversedArray(self, arr, n):
        if n == 0:
            return
        self.reversed_array.append(arr[n - 1])
        self.createReversedArray(arr, n - 1)

    def reverseArray(self, arr, n):
        self.createReversedArray(arr, n)
        return self.reversed_array


# {
# Driver Code Starts
# Initial Template for Python 3
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.reverseArray(Arr, n)
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
# } Driver Code Ends
