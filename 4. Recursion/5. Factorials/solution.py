# Brute Force : 
#   Time Complexity : O(k)
#   Space Complexity : O(k)

# Optimized :
#   Time Complexity : O(k)
#   Space Complexity : O(1)

#       where k is the number of factorials that can be computed before the new_val variable exceeds N
#       for very large values of N, we can say :
#       k ≈ log(N)

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
    
    def factorialNumbersOptimized(self, N):
        factorials_list = []
        curr_factorial = 1
        next_num = 2
        while(curr_factorial<=N):
            factorials_list.append(curr_factorial)
            curr_factorial *= next_num
            next_num+=1
        return factorials_list

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()

