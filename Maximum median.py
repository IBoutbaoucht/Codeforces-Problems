#Codeforces
n, k = map(int,input().split())

a = list(map(int,input().split()))
a.sort()

end = n//2
num_ele = 1

while k > 0 and end < n-1 :
    i = end
    while i < n and a[end] == a[i]:
        i += 1
    i -= 1
    num_ele += (i - end)
    end = i
    if end == n - 1:
        to_add = k // num_ele
        a[end] += to_add
        k = 0
        break
    else:
        to_add = (a[end + 1] - a[end]) * num_ele
        if k >= to_add:
            k -= to_add
            end += 1
            num_ele += 1
        else:
            to_add = k // num_ele
            a[end] += to_add
            k = 0

if end == n-1 and k > 0:
    a[end] += k//num_ele

print(a[end])