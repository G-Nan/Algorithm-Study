N, M = map(int, input().split())

basket = []

for _ in range(N):
    basket.append(0)

for _ in range(M):
    i,j,k = map(int, input().split())

    for n in range(i-1,j):
        basket[n] = k

print(*basket)