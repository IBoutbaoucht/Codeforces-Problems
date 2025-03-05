t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    k = 0
    while k < n and s[k] == "1" :
        k+=1
    if k == n :
        print(f"1 {n} 1 1")
        continue
    else:
        xors = ""
        for i in range(k,n) :
            if s[i] == "0" :
                xors+="1"
            else:
                xors+="0"

        l2 = r2 = 0
        start = 0
        end = 0
        while start < k :
            while start < k and s[start] != xors[0]:
                start += 1
            end = start
            while end < n and end-start < n-k and s[end] == xors[end - start]:
                end += 1
            if r2-l2 < end-start and start < k :
                l2 = start
                r2 = end
            start+=1

        print(f"{l2+1} {l2+n-k} 1 {n} ")

