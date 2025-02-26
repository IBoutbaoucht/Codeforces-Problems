t = int(input())
for _ in range(t):
    m = int(input())
    yes = True
    steps = 0
    A = list(map(int,input().split()))
    k = 1
    while len(A) > 1 and yes :
        B = []
        for j in range(0,len(A)-1,2):
            if abs(A[j] - A[j + 1]) != k:
                yes = False
                break
            elif (A[j+1] - A[j]) != k:
                steps+=1
        for i in range(0,len(A)-1,2):
            B.append(max(A[i],A[i+1]))
        A = B
        k*=2

    if yes :
        print(steps)
    else:
        print(-1)
