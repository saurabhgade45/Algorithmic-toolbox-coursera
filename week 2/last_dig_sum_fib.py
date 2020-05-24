n = int(input())

if n<=1:
    print(n)  
    quit()

lesser = (n+2)%60
if lesser==1:
    print(0)
    quit()
elif lesser==0:
    print(9)
    quit()
def fibo(n):
    a,b = 0, 1
    c = 1
    for _ in range(2,lesser+1):
        c = c+b
        
        b, a = a+b, b
    c = c%10
    print(c)
fibo(lesser)