from collections import Counter
t = int(input())
res = []
for _ in range(t):
    n,k = map(int,input().split())
    A = list(map(int,input().split()))
    d = Counter(A)
    l = float('inf')
    r = -l
    visited = set()
    for e in d :
        if d[e] >= k :
            if e not in visited :
                le = e
                re = e
                while re in d and d[re] >= k:
                    visited.add(re)
                    re+=1
                while le in d and d[le] >= k :
                    le-=1
                    visited.add(le)
                if re - le > r - l :
                    r = re
                    l = le
    if r - l < 0 :
        res.append([-1,""])
    else:
        res.append([l+1,r-1])


for e in res :
    print(e[0], e[1])