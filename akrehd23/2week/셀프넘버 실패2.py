N = []
A = []

for i in range(1, 10001):
    A.append(i)
    i_list = i + sum(map(int, str(i)))

    if(i_list <= 10000):
        N.append(i_list)

set(N)

for j in N:
    if(j in A):
        A.remove(j)
    else:
        print(j)