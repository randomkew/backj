a=int(input())
b=int(input())
sum=0
s=0
for i in range(b,a,-1):
    d=0
    if(i==1):
        continue
    else:
        for j in range(2,i):
            if(i%j==0):
                d=1
                break
    if(d==0):
        s=i
        sum+=i
if(sum==0):
    print(-1)
else:
    print(sum)
    print(s)