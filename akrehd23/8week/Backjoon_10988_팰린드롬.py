N = int(input())

A = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
L = []

for _ in range(len(A)):
    L.append(0)

gg = True

for _ in range(N):
    S = str(input())

    L[A.index(str(S[0]))] += 1

for i in range(0, len(L)):
    if L[i] >= 5:
        print(A[i], end="")
        gg = False

if gg == True:
    print('PREDAJA')