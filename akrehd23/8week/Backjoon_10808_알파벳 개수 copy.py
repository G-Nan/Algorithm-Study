S = str(input())

A = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
L = []

for _ in range(len(A)):
    L.append(0)

for i in S:
    L[A.index(str(i))] += 1

print(*L)