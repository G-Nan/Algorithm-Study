a1, a0=map(int,input().split())
c=int(input())
n=int(input())
fn=a1*n+a0
if fn>c*n:
    print(0)
if fn<c*n:
    print(1)