a="1011010"
count=0
ans=0
for i in range(len(a)):
    if a[len(a)-1-i]=='1':
        ans+=2**count
    count+=1
print("binary%s equivalent to %d indecimal"%(a,ans))
    