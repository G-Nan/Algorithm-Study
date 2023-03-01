N = []
A = []

for i in range(1, 10001):
    i_list = i + sum(map(int, str(i)))

    if(i_list <= 10000):
        N.append(i_list)

for j in range(1, 10001):
    if(j not in N):
        A.append(j)

print(A)