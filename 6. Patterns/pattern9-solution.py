class Solution:
    def printDiamond(self, N):
        for i in range(0,2*N):
            for j in range(0,2*N):
                if(i<N):
                    if(j in range(N-1-i,N+i)):
                        if(N%2 != 0):
                            if(i%2 == 0 and j%2==0):
                                print("*",end=" ")
                            elif(i%2 != 0 and j%2!=0):
                                print("*",end=" ")
                        else:
                            if(i%2 == 0 and j%2!=0):
                                print("*",end=" ")
                            elif(i%2 != 0 and j%2==0):
                                print("*",end=" ")
                    elif(j<N-1-i):
                        print(" ",end="")
                else:
                    if(j in range(-(N-i),(3*N-i))):
                        if(N%2 == 0):
                            if(i%2 == 0 and j%2==0):
                                print("*",end=" ")
                            elif(i%2 != 0 and j%2!=0):
                                print("*",end=" ")
                        else:
                            if(i%2 == 0 and j%2!=0):
                                print("*",end=" ")
                            elif(i%2 != 0 and j%2==0):
                                print("*",end=" ")
                    elif(j<-(N-i)):
                        print(" ",end="")
            print("\n",end="")


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printDiamond(N)