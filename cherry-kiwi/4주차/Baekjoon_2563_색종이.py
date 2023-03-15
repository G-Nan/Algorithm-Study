paper=[[0 for _ in range(101)] for _ in range(101)] #가로 100 세로 100

num=int(input())

for i in range(num):
    x, y=list(map(int, input().split()))
    
    for row in range(x, x+10):
        for col in range(y, y+10):
            paper[row][col]=1
sum=0

for j in paper:
    sum+=j.count(1)

print(sum)