a=list(input().lower())
sum=0
print(a)
for i in range(len(a)):
    if(ord(a[i])>=97 and ord(a[i])<100):#2
        sum+=3
    elif(ord(a[i])>=100 and ord(a[i])<103):#3
        sum+=4
    elif(ord(a[i])>=103 and ord(a[i])<106):#4
        sum+=5
    elif(ord(a[i])>=106 and ord(a[i])<109):#5
        sum+=6
    elif(ord(a[i])>=109 and ord(a[i])<112):#6
        sum+=7
    elif(ord(a[i])>=112 and ord(a[i])<116):#7
        sum+=8
    elif(ord(a[i])>=116 and ord(a[i])<119):#8
        sum+=9
    elif(ord(a[i])>=119 and ord(a[i])<123):#9
        sum+=10
    print(sum)
