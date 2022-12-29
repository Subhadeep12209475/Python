n=8
while n>0:
    c=1
    a=1
    b=1
    count=2
    while count<n:
        c=a+b
        a=b
        b=c
        count+=1
    print("fibonacciof%dis%d",(n,c))
    n-=1