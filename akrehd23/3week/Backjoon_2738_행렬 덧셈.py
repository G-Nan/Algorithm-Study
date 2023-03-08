N, M = map(int, input().split())
R = []
R2 = []

for _ in range(0, N):
    R.append(list(map(int, input().split())))

for _ in range(0, N):
    R2.append(list(map(int, input().split())))

for i in range(0, N):
    for j in range(0, M):
        R[i][j] += R2[i][j]

    print(*R[i])

