t= int(input())

for i in range(t):
    a,b=map(int,input().split())
    c=b-a
    sum=0
    x=1
    
    while(1):
        if(c>2*x):
            c-=2*x
            sum+=2
            x+=1
        elif(c>x):
            sum+=2
            break
        elif(c<=x):
            print(c)
            sum+=1
            break
    print(sum)
    

