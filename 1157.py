aaa=input().lower()
lll=0
st=-1
res=''
for j in range(97,123):
    lll=aaa.count(chr(j))
    print(f'{chr(j)}의 숫자는{lll}')
    if(lll>=st):
        if(lll==st):
            res='?'
        else:
            res=chr(j)
        st=lll
    print(res)
print(res.upper())
        

