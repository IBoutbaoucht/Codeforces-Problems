t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    max_score = -float('inf')
    best_i = 0
    best_j = 0

    for i in range(n):
        current_sum = 0
        current_max = 0
        current_best_j = i
        for j in range(i + 1, n):
            if a[j] < a[i]:
                current_sum += 1
            elif a[j] > a[i]:
                current_sum -= 1

            if current_sum > current_max:
                current_max = current_sum
                current_best_j = j

        if current_max > max_score :
            max_score = current_max
            best_i = i
            best_j = current_best_j

    print(best_i + 1, best_j + 1)