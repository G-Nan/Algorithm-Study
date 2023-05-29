import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    w = list(input())
    k = int(input())

    dic_w = {}
    
    min_len = len(w)
    max_len = 0

    for i, j in enumerate(w):
        if dic_w.get(j):
            dic_w[j].append(i)
        else:
            dic_w[j] = [i]

    for key, value in dic_w.items():
        if len(value) < k:
            continue

        for i in range(len(value) - (k-1)):
            len_word = value[i+k-1] - value[i] + 1
            min_len = min(min_len, len_word)
            max_len = max(max_len, len_word)

    if min_len == len(w) and max_len == 0:
        print(-1)
    else:
        print(min_len, max_len)