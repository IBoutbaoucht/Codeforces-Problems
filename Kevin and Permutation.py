t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    L = []
    current = n//k+1
    start = 1
    for i in range(n):
        if (i+1)%k == 0 :
            L.append(start)
            start+=1
        else:
            L.append(current)
            current+=1

    for e in L:
        print(e, end=" ")
    print()
