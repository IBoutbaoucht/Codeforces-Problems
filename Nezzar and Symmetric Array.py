from collections import Counter
res = []
t = int(input())
for _ in range(t):
    n = int(input())
    L = list(map(int, input().split()))
    frequencies = Counter(L)

    if any(frequencies[d] != 2 for d in frequencies):
        res.append("NO")
        continue
    L = sorted(set(L))
    if (L[-1] == 0 or L[-1]%(2*n) != 0 ) :
        res.append("NO")
        continue

    check = True
    current = L[-1]//(2*n)
    for i in range(n-2,-1,-1):
        if (L[i+1]-L[i]) % (2*(i+1)) != 0 :
            check = False
            break
        else:
            current = current - (L[i + 1] - L[i]) // (2 * (i + 1))
            if current <= 0:
                check = False
                break

    res.append("YES" if check else "NO")


for p in res :
    print(p)