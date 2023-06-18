# Time complexity : O(log n)
# Space complexity : O(1)


class Solution:
    def reversedBits(self, X):
        binary_num = format(X, "032b")
        binary_num_reversed = binary_num[::-1]
        return int(binary_num_reversed, 2)


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        X = int(input())

        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends


# Complexity Analysis:

# Time Complexity:

# - The line binary_num = format(X, "032b") converts the number X to its binary representation, which takes O(log X) time complexity since the number of digits in the binary representation is proportional to the logarithm of X (base 2).
# - The subsequent line binary_num_reversed = binary_num[::-1] reverses the binary string, which takes O(32) = O(1) time complexity since the length of the string is fixed at 32.
# - Finally, the line return int(binary_num_reversed, 2) converts the reversed binary string back to decimal, which takes O(32) = O(1) time complexity since the length of the string is fixed at 32.
# - Therefore, the overall time complexity of the code is O(log X).

# Space Complexity:

# - The code creates three string variables: binary_num, binary_num_reversed, and the temporary string representation of X during the formatting operation.
# - The space used by these strings depends on the length of the binary representation, which is fixed at 32 characters.
# - Therefore, the space complexity of the code is O(32) = O(1), as the space usage is constant and does not scale with the input size.
