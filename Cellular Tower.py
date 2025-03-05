n , m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

r = 0
i = 0
j = 0
for ai in a :
    while j < m and b[j] < ai :
        j+=1
    if j == 0 :
        r = max(r, b[j]-ai)
        continue
    if j == m :
        r = max(r, a[-1]-b[-1])
        break
    i = j-1
    r = max(r,min(ai-b[i],b[j]-ai))


print(r)