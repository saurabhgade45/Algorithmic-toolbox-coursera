def max_pair(number1):
    number = []
    maxp = 0
    for i in range(number1):
        n1 = int(input())
        number.append(n1)
    for i in range(number1):
       
        for j in range(i+1,number1):
            if (number[i]*number[j]>maxp):
                maxp = number[i]*number[j]
    return maxp



if __name__=="__main__":
    number = int(input())
    x = max_pair(number)
    print(x)