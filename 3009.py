a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())
answer1=0;answer2=0;
if(a-c==0):
    answer1=e
elif(a-e==0):
    answer1=c
else:
    answer1=a
if(b-d==0):
    answer2=f
elif(b-f==0):
    answer2=d
else:
    answer2=b
print(answer1, answer2)
