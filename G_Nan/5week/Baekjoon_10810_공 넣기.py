x0 = list(map(int, input().split()))
basket = [0 for _ in range(x0[0])]
ball = [list(map(int, input().split())) for _ in range(x0[1])]

for i in ball:
    basket[i[0]-1:i[1]] = [i[2] for _ in range(i[0]-1,i[1])]
    
print(*basket)