

def fastgcd(a,b):
    if b == 0:
        return a
    else:
        if a > b:
            ad = a%b
            return fastgcd(b,ad)

        else:
            
            bd  = b%a
            return fastgcd(a,bd)

def lcmfun(a,b):
    lcm1 = (a*b)/fastgcd(a,b)
    return lcm1

if __name__ =="__main__":
    n1,n2 = map(int,input().split())
    x = lcmfun(n1,n2)
    x = int(x)
    print(x)