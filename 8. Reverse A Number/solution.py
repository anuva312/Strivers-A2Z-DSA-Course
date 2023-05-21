#User function Template for python3

class Solution:
    def reversedBits(self, X):
        print("XORed",X^X)
        binary_num = format(X, '032b')
        binary_num_reversed = binary_num[::-1]
        return int(binary_num_reversed,2)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends