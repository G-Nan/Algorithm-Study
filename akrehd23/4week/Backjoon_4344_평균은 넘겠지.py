import sys
input = sys.stdin.readline

C = int(input())

for _ in range(C):
    T = 0
    C = 0

    N = list(map(int, input().split()))

    for i in range(1, len(N)):
        T += N[i]

    T /= N[0]

    for i in N[1:]:
        if(i > T):
            C += 1

    R = C/N[0]*100

    print(f"{R:.3f}%")