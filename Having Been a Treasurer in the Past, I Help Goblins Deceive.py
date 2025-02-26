import math

t = int(input())
for _ in range(t):
    n = int(input())
    D = {'-':0,'_':0}
    s = input()
    for i in s :
        D[i]+=1

    print((((D['-'])//2)*(math.ceil((D['-'])/2)))*D['_'])
