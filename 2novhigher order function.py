def Summation(n,term):
    total,K=0,1
    while K<=n:
        total,K= total+term(K),K+1
    return total
def term(x):
    return  x**3
def CubeSum (n):
    return Summation(n,term)
print(CubeSum(3))