import math

t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    if n == 1:
        print(x)
        continue
    b = bin(x)[2:][::-1]
    if n > x :
        if b == '1'*len(b) :
            for k in range(x):
                print(k,end=' ')
            for u in range(n-x):
                print(x,end=' ')
            print()
            continue
        else:
            i = 0
            while i < len(b) and b[i] == '1' :
                i+=1
            if i>0 : i-=1

            for j in range(2**i+1):
                print(j,end=' ')
            for j in range(n-2**i-1):
                print(x,end=' ')
            print()
    else:
