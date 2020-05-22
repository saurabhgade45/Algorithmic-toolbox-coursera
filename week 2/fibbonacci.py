n=int(input())

def sumlastagain(n):
    if n<=1:
        print(n)
        quit()
    a = 0
    b = 1
    c=0
    for i in range(n):
        c = c + b
        a,b = b,a+b

    
    print(c)

sumlastagain(n)