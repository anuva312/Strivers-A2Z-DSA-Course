#User function Template for python3
import math

class Solution:
    def getSumOfDivisors(self, N):
        sum = 0
        i = 1
        while(i <= math.sqrt(N)):
            if(N%i == 0):
                factor = N/i
                if(factor == i):
                    sum = sum + factor
                else:
                     sum = sum + i +factor
            i =i +1
        return sum
    	       
    def sumOfDivisors(self,N):
        sum = 0
        for i in range(N+1):
            sum = sum +self.getSumOfDivisors(i)
        return int(sum)
    
    def sumOfDivisorsOptimized(self,N):
        sum = 0
        for i in range(1,N+1):
            sum = sum + i * (N//i)
        return sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisorsOptimized(N)
        print(ans)
# } Driver Code Ends