# Time Complexity : O(log n)
# Space Complexity : O(1)


class Solution:
    def armstrongNumber(ob, n):
        num = n
        sum = 0
        length = len(str(n))
        while n > 0:
            rem = n % 10
            sum = sum + rem**length
            n = n // 10
        if num == sum:
            return "Yes"
        return "No"

    def isArmstrongNumber(ob, n):
        num = n
        sum_of_cubes = 0
        digit_count = 0
        temp = n

        # Count the number of digits in n
        while temp > 0:
            temp //= 10
            digit_count += 1

        temp = n

        # Calculate the sum of cubes of digits
        while temp > 0:
            digit = temp % 10
            sum_of_cubes += digit**digit_count
            temp //= 10

        if num == sum_of_cubes:
            return "Yes"
        return "No"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
