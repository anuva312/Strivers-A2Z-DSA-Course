# Time Complexity: O(N)
# Space Complexity: O(N) (due to the call stack)
# Auxiliary Space: O(1)

class Solution: 
    def printNos(self,N,new_val =1):
        if new_val>N:
            return
        print(new_val,end=" ")
        self.printNos(N,new_val+1)

    def printNosAlternative(self,N):
        if(N>0):
            self.printNos(N-1)
            print(N,end=" ")

def main():
    T=int(input())
    while(T>0):
        N=int(input())
        ob=Solution()
        ob.printNos(N)
        print()
        T-=1

if __name__=="__main__":
    main()