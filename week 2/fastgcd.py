

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



if __name__ =="__main__":
    n1,n2 = map(int,input().split())
    x = fastgcd(n1,n2)
    print(x)