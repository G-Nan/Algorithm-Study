x0 = int(input())
x = [list(map(int, input().split())) for _ in range(x0)]

coord = []
for c in x:
    for i in range(10):
        for j in range(10):
            coord.append([c[0] + i, c[1] + j])
            
print(len(set(list(map(tuple, coord)))))