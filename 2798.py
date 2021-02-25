x,y=map(int,input().split())
a=list(map(int,input().split()))
sum=0
for i in range(x-2):
    for j in range(i+1,x-1):
        for l in range(j+1,x):
            if(a[i]+a[j]+a[l]<=y):
                if(sum<a[i]+a[j]+a[l]):
                    sum=a[i]+a[j]+a[l]
                    print(a[i],a[j],a[l], sum)
            if(sum==y):
                break
print(sum)

