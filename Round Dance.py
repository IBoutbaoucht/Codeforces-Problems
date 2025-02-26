import math

t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int,input().split()))
    G = {}
    for i in range(n):
        if i+1 not in G :
            G[i + 1] = [0]
        if A[i] not in  G :
            G[A[i]] = [0]
        G[i+1][0] = A[i]
        G[A[i]].append(i+1)
    sub_Graphs = 0
    cycles = 0
    visited = [False]*(n+1)
    frees = []
    for i in range(1,n+1):
        if not visited[i]:
            L  = set()
            stack = [i]
            while stack :
                current = stack.pop()
                visited[current] = True
                if len(G[current]) == 1 or ( len(G[current]) == 2 and G[current][0] == G[current][1] ):
                    L.add(current)
                for x in G[current]:
                    if not visited[x]:
                        stack.append(x)
            frees.append(len(L))

    cycles = frees.count(0)
    ones = frees.count(1)
    twos = frees.count(2)
    minima = math.ceil(ones/2) + cycles + min(1,twos)
    maxima = len(frees)

    print(minima,maxima)

