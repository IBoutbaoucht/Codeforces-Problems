t = int(input())
for _ in range(t):
    n = int(input())
    res = min(n+1,3)

    if n >= 15 :
        res += (n // 15 - 1) * (3)
        res += min(3, (n % 15)+1)
    print(res)