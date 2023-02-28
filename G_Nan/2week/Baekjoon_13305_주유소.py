x1 = int(input())
x2 = list(map(int, input().split( )))
x3 = list(map(int, input().split( )))
answer = 0

min_oil = x3[0]

for i in range(x1 - 1):
    if min_oil > x3[i]:
        min_oil = x3[i]
    answer += min_oil * x2[i]
    
print(answer)