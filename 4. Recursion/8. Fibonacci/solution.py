# Time Complexity: O(n)
# Space Complexity: O(n)
# Auxiliary Space: O(n)

class Solution:
    def __init__(self):
        self.fibonacci_list = []

    def get_fibonacci_list(self):
        return self.fibonacci_list

    def update_fibonacci_list(self, n, curr_count):
        if curr_count >= n:
            return
        prev_value = self.fibonacci_list[-1]
        second_prev_value = self.fibonacci_list[-2]
        self.fibonacci_list.append(prev_value + second_prev_value)
        self.update_fibonacci_list(n, curr_count + 1)

    # Function to return list containing first n fibonacci numbers.
    def printFibb(self, n):
        if n < 0:
            return []
        elif n == 1:
            return [1]
        self.fibonacci_list = [1, 1]
        self.update_fibonacci_list(n, 2)
        return self.get_fibonacci_list()

if __name__ == "__main__":
    t = int(input())
    for tcs in range(t):
        n = int(input())
        res = Solution().printFibb(n)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
