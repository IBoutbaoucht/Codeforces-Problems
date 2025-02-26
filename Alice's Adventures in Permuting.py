t = int(input())
for _ in range(t):
    n,b,c = map(int,input().split())
    if n == 1 :
        if c == 0 :
            print(0)
        else:
            print(1)
    elif n == 2 :
        if c == 0 and b == 1:
            print(0)
        elif c == 0 or c == 1 :
            print(1)
        else:
            print(2)
    elif n <= c:
        print(n)
    elif b > 0 :
        if (n-c-1)%b == 0 :
            i = (n - c - 1) // b
            print(n-(i+1))
        else:
            print(-1)
    else:
        if c == 0 :
            print(-1)
        else:
            print(n - 1)





