a=int(input())
for q in range(a):
    num,alph=input().split()
    for i in range(len(alph)):
        for j in range(int(num)):
            print(alph[i], end="")
    print()
"""
t = int(input())
for i in range(t):
    num, s = input().split()
    text = ''
    for i in s:
        text += int(num) * i
    print(text)
"""

