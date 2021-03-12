x=int(input())
y=list(map(int,input().split()))
y = sorted(y)
sum=0
for i in range(x):
    sum+=y[i]*(x-i)
    print(sum)
print(sum)