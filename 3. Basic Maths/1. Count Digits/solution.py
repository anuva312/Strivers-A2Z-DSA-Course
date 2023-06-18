# Time complexity : O(log N)
# Space complexity : O(1)
class Solution:
    def evenlyDivides(self, N):
        num = N
        count = 0
        while num > 0:
            rem = num % 10
            if rem != 0 and N % rem == 0:
                count = count + 1
            num = num // 10
        return count


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.evenlyDivides(N))
