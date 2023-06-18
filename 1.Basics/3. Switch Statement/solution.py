# Python version used should be 3.10 or above to suport switch cases

import math;
class Solution:
    def switchCase(self, choice, arr):
        match choice:
            case 1:
                return math.pi *arr[0]*arr[0]
            case 2:
                return arr[0]*arr[1]
            case _:
                return "Input choice should be either 1 or 2"


if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        choice = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        if choice == 1:
            res = ob.switchCase(choice, arr)
            print(res)
        else:
            res = ob.switchCase(choice, arr)
            print(int(res))