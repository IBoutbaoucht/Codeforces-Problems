t = int(input())
for _ in range(t):
    n = int(input())
    elements = []
    points = {}
    sums = [0]*400001
    for k in range(n):
        l,r = map(int,input().split())
        elements.append((l,r))
        if l == r :
            if l in points : points[l] += 1
            else: points[l] = 1
            sums[l] = 1
    for i in range(1,2*n):
        sums[i]+=sums[i-1]
    s = ""
    for element in elements :
        if element[1] == element[0] :
            if points[element[0]] <= 1 :
                s+="1"
            else:
                s+="0"
        elif sums[element[1]]-sums[element[0]-1] < element[1] - element[0] + 1 :
            s+="1"
        else:
            s+="0"


    print(s)