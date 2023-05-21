class Solution:
    def armstrongNumber (ob, n):
        num = n
        sum = 0
        length = len(str(n))
        while(n>0):
            rem = n%10
            sum = sum + rem**length
            n = n//10
        if(num == sum):
            return "Yes"
        return "No"
        
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))