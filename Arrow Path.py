t = int(input())
for _ in range(t):
    n = int(input())
    L1 = input()
    L2 = input()
    G = {}
    for j in range(1, n + 1):
        G[(1, j)] = []
        if j % 2 == 0:
            if L1[j - 1] == '>':
                G[(1, j)].append((1, j + 1))
            elif L1[j - 1] == '<':
                G[(1, j)].append((1, j - 1))
        else:
            G[(1, j)].append((2, j))
            if j - 1 > 0:
                G[(1, j)].append((1, j - 1))
            if j + 1 <= n:
                G[(1, j)].append((1, j + 1))

    for j in range(1, n + 1):
        G[(2, j)] = []
        if j % 2 != 0:
            if L2[j - 1] == '>':
                G[(2, j)].append((2, j + 1))
            elif L2[j - 1] == '<':
                G[(2, j)].append((2, j - 1))
        else:
            G[(2, j)].append((1, j))
            if j - 1 > 0:
                G[(2, j)].append((2, j - 1))
            if j + 1 <= n:
                G[(2, j)].append((2, j + 1))

    vis = [[False] * (n + 1) for _ in range(3)]
    stack = [(1, 1)]
    while stack:
        current = stack.pop()
        r, c = current
        vis[r][c] = True
        for a in G[current]:
            ar, ac = a
            if not vis[ar][ac]:
                stack.append(a)

    print("YES" if vis[2][n] else "NO")