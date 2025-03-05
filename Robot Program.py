t = int(input())
r = []
for _ in range(t):
    n , x , k = map(int,input().split())
    B = input()
    A = []
    for a in B :
        A.append(a)
    res = 0
    i = 0
    while k > 0 and x != 0 and i < n:
        k-=1
        if A[i] == 'L' :
            x-=1
        else:
            x+=1
        i+=1
    if x == 0 :
        res+=1
        tour = 1
        i = 1
        if A[0] == 'L' :
            x = -1
        else:
            x = 1
        while i < n and x != 0 :
            if A[i] == 'L':
                x -= 1
            else:
                x += 1
            i += 1
            tour +=1
        if x == 0 :
            res+= k//tour

    r.append(res)

for rres in r :
    print(rres)

