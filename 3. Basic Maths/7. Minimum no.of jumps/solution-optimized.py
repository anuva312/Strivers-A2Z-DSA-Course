# Time complexity : O(n)
# Space complexity : O(1)


class Solution:
    def minJumps(self, arr, n):
        if n <= 1:
            return 0
        if arr[0] == 0:
            return -1

        no_of_jumps = 1
        remaining_steps = arr[0]
        possible_reach = arr[0]

        for i in range(1, n):
            if i == n - 1:
                return no_of_jumps
            possible_reach = max(possible_reach, i + arr[i])

            remaining_steps -= 1

            if remaining_steps == 0:
                if i >= possible_reach:
                    return -1
                no_of_jumps += 1
                remaining_steps = possible_reach - i
        return -1


# {
# Driver Code Starts
# Initial Template for Python 3
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr, n)
        print(ans)
# } Driver Code Ends
