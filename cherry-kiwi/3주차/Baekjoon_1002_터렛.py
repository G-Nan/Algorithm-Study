#원의 접점을 구하는 문제였다!!!;;;;;
import math

t=int(input())
#원을 그리고 두 원의 교집합 안의 정수들의 집합
for i in range(t):
    x1, y1, r1, x2, y2, r2=map(int, input().split())
    d=math.sqrt((x2-x1)**2+(y2-y1)**2) #원과 원과의 distance

    #①접점이 무수한(-1개) 경우 = 원이 완벽하게 일치할 때
    if d==0 and r1==r2:
        print(-1)
    #②접점이 1개인 경우 = 내접abs(r1-r2)=d or 외접(r1+r2=d)
    elif abs(r1-r2)==d or (r1+r2)==d:
        print(1)
    #③접점이 2개인 경우 
    elif abs(r1-r2) < d < r1+r2:
        print(2)
    #④접점이 없는(0개) 경우
    else: print(0)