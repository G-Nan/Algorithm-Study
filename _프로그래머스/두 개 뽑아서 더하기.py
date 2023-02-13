def Self():
    for i in range(1, 10001):
        i_list =[]
        S = i
        i_list = list(map(int, str(i)))
        for j in range(len(i_list)):
            S += i_list[j]
        if(S in S_list):
            S_list.remove(S)
        else:
            pass

        print(S_list)


S_list = []
for k in range(1, 10001):
    S_list.append(k)

Self()