a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
b = input()
for i in a:
    print(i)
    b = b.replace(i, 'a')
print(len(b))