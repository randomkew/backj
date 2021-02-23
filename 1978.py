a=int(input())
b=list(map(int,input().split()))
sum=0
for i in range(a):
    d=0
    c=b[i]
    if(c==1):
        continue
    else:
        for j in range(2,c):
            if(c%j==0):
                print(c)
                d=1
                break
    if(d==0):
        sum+=1
print(sum)
        

    
