import string 

class Solution:
    def printTriangle(self, N):
        alphabets = list(string.ascii_uppercase)
        for i in range(0,N):
            count = 0
            for j in range(0,N+i):
                if(j in range(N-1-i,N+i)):
                    if(j<N):
                        print(alphabets[count],end="")
                        count=count+1
                    elif(j==N):
                        count=count-2
                        print(alphabets[count],end="")
                    else:
                        count=count-1
                        print(alphabets[count],end="")
                else:
                    print(" ",end="")
            print("\n",end="")

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)