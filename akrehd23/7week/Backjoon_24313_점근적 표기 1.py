a1,a0 = map(int, input().split())
c = int(input())
n = int(input())

f = (a1*n) + a0

e = 1

if(c >= a1):
    if (f <= c * n):
        e = 1
    else:
        e = 0
else:
    e = 0

print(e)