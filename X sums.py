t = int(input())

def get_left_diagonals(matrix):
    diagonals = {}
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    for row in range(rows):
        for col in range(cols):
            diff = row - col
            if diff not in diagonals:
                diagonals[diff] = []
            diagonals[diff].append(matrix[row][col])

    return ([sum(diagonals[key]) for key in sorted(diagonals.keys())])


def get_right_diagonals(matrix):
    diagonals = {}
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    for row in range(rows):
        for col in range(cols):
            sum_index = row + col
            if sum_index not in diagonals:
                diagonals[sum_index] = []
            diagonals[sum_index].append(matrix[row][col])

    return [sum(diagonals[key]) for key in sorted(diagonals.keys())]


for _ in range(t):
    A = []
    n, m = map(int, input().split())
    for i in range(n):
        L = list(map(int, input().split()))
        A.append(L)
    D1 = get_right_diagonals(A)
    D2 = get_left_diagonals(A)
    r = 0
    for i in range(n):
        for j in range(m):
            r = max(r, D1[i + j] + D2[i - j + m-1]-A[i][j])
    print(r)

