def substract (a,b):
    return b-a
def divide (a,b):
    return int(a/b)
def pow (b,a):
    return a**b
def modolus (a,b):
    return b%a

a=int(input("Enter the number"))
b=int(input("Enter the number"))
print(substract(b,a))
print(divide(b,a))
print(pow(a,b))
print(modolus(b,a))