# User function Template for python3
class Solution:
    def __init__(self):
        self._result = 1

    def get_result(self):
        return self._result

    def checkPalindrome(self, S, left, right):
        if left >= right:
            return
        if S[left] != S[right]:
            self._result = 0
            return
        self.checkPalindrome(S, left + 1, right - 1)

    def isPalindrome(self, S):
        self.checkPalindrome(S, 0, len(S) - 1)
        return self.get_result()


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.isPalindrome(S)
        print(answer)

# } Driver Code Ends
