import math

def check_prime(n):
    if(n<2):
        return "No"
    for i in range(2,math.floor(math.sqrt(n)+1)):
        if(n%i == 0):
            return "No"
    return "Yes"


if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        num = int(input())
        print(check_prime(num))