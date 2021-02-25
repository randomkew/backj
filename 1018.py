x,y=map(int,input().split())
a=[]
for _ in range(y):
    a.append((input()))
b=[]
for i in range(x-7):
    for j in range(y-7):
        www=0
        bbb=0
        for I in range(i,i+8):
            for J in range(j,j+8):
                if(I+J)%2==0:
                    if(a[I][J]!='W'):
                        www+=1
                    if(a[I][J]!='B'):
                        bbb+=1
                else:
                    if(a[I][J]!='B'):
                        www+=1
                    if(a[I][J]!='W'):
                        bbb+=1
        b.append(www)
        b.append(bbb)
print(min(b))

        
