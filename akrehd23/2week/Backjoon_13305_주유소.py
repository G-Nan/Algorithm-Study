import sys
input = sys.stdin.readline


N = int(input())

D = list(map(int, input().split()))

P = list(map(int, input().split()))

DT = sum(D)

DT -= D[0]

T = 0

T += P[0] * D[0]

for i in range(1, N-1):
    if(P[i-1] < P[i]):
        T += P[i-1] * D[i]
    else:
        T += P[i] * D[i]
    DT -= D[i]

print(T)