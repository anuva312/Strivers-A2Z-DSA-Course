class Solution:
    def findGCDOptimized(self,A,B):
        if(B == 0):
            return A
        return self.findGCDOptimized(B,A%B)
    
    def findGCD(self,A,B):
        if(A == 0):
            return A
        if(B == 0):
            return B
        if(A>B):
            if(A%B == 0):
                return B
            return self.findGCD(A-B,B)
        else:
            if(B%A == 0):
                return A
            return self.findGCD(A,B-A)
    def lcmAndGcd(self, A , B):
        gcd = self.findGCDOptimized(A,B)
        lcm = int((A*B)/gcd)
        return [lcm,gcd]
        

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])