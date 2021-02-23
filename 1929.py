a,b=map(int,input().split())
for i in range(a,b+1):
    count=0
    for j in range(1, int(i**0.5)+1):
        if i %j==0:
            count +=1
            if count>1:
                break
    if count==1:
        print(i)

