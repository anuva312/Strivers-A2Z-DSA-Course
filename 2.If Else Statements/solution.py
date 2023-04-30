class Solution:
    def compareNM(self, n : int, m : int) -> str:
        if n<m:
            return "lesser"
        elif n>m:
            return "greater"
        else:
            return "equal"

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        obj = Solution()
        res = obj.compareNM(n, m)
        
        print(res)