a="1011010"
b="1000110"
ans=""
len1=len(a)
for i in range (len1):
    if((a[len1-1-i]=='1'and b[len1-1-i]=='0')or(a[len1-1-i]=='0'and b[len1-1-i]=='1')):
            ans="1"+ans
    else:
            ans="0"+ans
print(ans)