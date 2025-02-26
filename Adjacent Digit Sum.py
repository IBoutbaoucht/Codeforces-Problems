#Codeforces
t = int(input())

for _ in range(t):
    x,y = map(int,input().split())
    if y>= x :
        if y == x+1 : print('Yes')
        else : print('No')
    else:
        if (x-y+1)%9 == 0 :
            print('Yes')
        else:
            print('No')