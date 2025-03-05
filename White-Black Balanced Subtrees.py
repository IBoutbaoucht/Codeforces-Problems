BlackWhites = {}
G = {}

def BlackWhite(vertice,s):
    if s[vertice - 1] == "B":
        BlackWhites[vertice] = [1, 0]
    else:
        BlackWhites[vertice] = [0, 1]
    if vertice not in G :
        return BlackWhites[vertice]
    for child in G[vertice]:
        BlackWhites[child] = BlackWhite(child,s)
        BlackWhites[vertice] = [BlackWhites[vertice][0]+BlackWhites[child][0],BlackWhites[vertice][1]+BlackWhites[child][1]]
    return BlackWhites[vertice]

res = []

t= int(input())
for _ in range(t):
    BlackWhites = {}
    G = {}
    n = int(input())
    a = list(map(int,input().split()))
    s = input()
    for i in range(n-1) :
        if a[i] not in G :
            G[a[i]] = []
        G[a[i]].append(i+2)
    BlackWhite(1,s)
    r = 0
    for i in range(1,n+1):
        if BlackWhites[i][0] == BlackWhites[i][1] :
            r+=1
    res.append(r)


for r in res :
    print(r)

