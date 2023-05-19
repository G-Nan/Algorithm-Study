import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

L = {}

for _ in range(N):
    S = input().rstrip()

    if (len(S) >= M):
        if (S in L):
            L[S] += 1
        else:
            L[S] = 1

L = sorted(L, key=lambda x: x)

print(*L, sep="\n")

