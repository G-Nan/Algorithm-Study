N = list(map(int, input().split()))

T = 0
C = 0

while(T < N[2]):
    C += 1
    T += N[0]
    if(T >= N[2]):
        break
    T -= N[1]

print(C)