S = str(input())

N = 0
L = []
R = []

if len(S)%2 != 0:
    N = len(S) - 1

    for i in range(0, N//2):
        L.append(S[i])
        R.append(S[i])
    L.append(S[N//2])
    R.reverse()

    for j in R:
        L.append(j)

else:
    N = len(S)

    for i in range(0, N//2):
        L.append(S[i])
        R.append(S[i])
    R.reverse()

    for j in R:
        L.append(j)

if S == ''.join(L):
    print(1)
else:
    print(0)