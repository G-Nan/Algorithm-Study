N = int(input())
paper = []

for _ in range(N):
    y, x = map(int, input().split())

    for i in range(y, y + 10):
        for j in range(x, x + 10):
            if (i, j) not in paper:
                paper.append((i, j))
set(paper)
print(len(paper))