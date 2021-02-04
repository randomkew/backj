for i in range(1,10000):
    W=False
    A=i
    for j in range(1,i+1):
        DR_one=j
        DR=list(map(int, str(j)))
        if(j<10 and A==DR_one*2):
            W=True
        if(j<100 and j>=10 and A==DR_one+DR[0]+DR[1]):
            W=True
        if(j<1000 and j>=100 and A==DR_one+DR[0]+DR[1]+DR[2]):
            W=True
    if(i>=1000):
        for j in range(i-100,i+1):
            DR_one=j
            DR=list(map(int, str(j)))        
            if(j<10000 and j>=1000 and A==DR_one+DR[0]+DR[1]+DR[2]+DR[3]):
                W=True
    if(W==False):
        print(i)