white = list(map(int, input().split(' ')))
chess = [1, 1, 2, 2, 2, 8]
black = [i - j for i, j in zip(chess, white)]
print(*black)