import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
memo = {input().rstrip() for _ in range(n)}

for i in range(m):
    keyword = input().rstrip().replace(' ', '').split(',')

    for key in keyword:
        if key in memo:
            memo.remove(key)
        
    print(len(memo))