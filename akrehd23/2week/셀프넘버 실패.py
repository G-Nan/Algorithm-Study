N = []

for i in range(1, 10001):
    S = i
    i_list = list(map(int, str(i)))
    for j in range(len(i_list)):
        S += i_list[j]

    if(S <= 10000):
        N.append(i)

for k in range(1, 10001):
    if k not in N:
        print(k)