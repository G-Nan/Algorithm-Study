import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())

    R1 = []
    R2 = []
    E = []

    C = 0

    for i in range(x1-r1, x1+r1+1):
        for j in range(y1-r1, y1+r1+1):
            if((abs(x1-i)+abs(y1-j)) == r1):
                R1.append(list(map(int, (i, j))))

    for k in range(x2-r2, x2+r2+1):
        for l in range(y2-r2, y2+r2+1):
            if((abs(x2-k)+abs(y2-l)) == r2):
                R2.append(list(map(int, (k, l))))

    E = list(set(R1).intersection(R2))

    if(len(E) <= 2):
        print(len(E))
    elif(C > 2):
        print(-1)