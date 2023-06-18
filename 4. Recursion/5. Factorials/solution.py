# User function Template for python3


class Solution:
    def __init__(self):
        self.factorials_list = []

    def findAllFactorialNumbers(self, N, curr_val=2):
        last_value = self.factorials_list[-1]
        new_val = last_value * curr_val
        if new_val > N:
            return
        self.factorials_list.append(new_val)
        self.findAllFactorialNumbers(N, curr_val + 1)

    def factorialNumbers(self, N):
        self.factorials_list.append(1)
        self.findAllFactorialNumbers(N)
        return self.factorials_list


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends
