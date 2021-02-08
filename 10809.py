al=list(map(str,input()))
al_len=len(''.join(al))

    
for i in range(97,123):
    e=-1
    for j in range(al_len):
        if(ord(al[j])==i):
            e=j
            break
    print(e, end=" ")
"""
word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위

for x in alphabet :
    print(word.find(chr(x)))
"""
