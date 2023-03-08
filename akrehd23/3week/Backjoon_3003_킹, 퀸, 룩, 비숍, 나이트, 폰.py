P = list(map(int, input().split()))
E = []

for i in range(0, 2):
    E.append(1 - P[i])

for j in range(2, 5):
    E.append(2 - P[j])

E.append(8 - P[5])

print(*E)
