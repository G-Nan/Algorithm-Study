import sys

input = sys.stdin.readline

n = int(input())
ex = input()

star = ex.index('*')
front = ex[:star]
back = ex[star + 1:]

for i in range(n):
    word = input()
    
    if len(word) < len(ex)-1:
        print('NE')
        continue
    if (word[:len(front)] == front) & (word[-len(back):] == back):
        print('DA')
    else:
        print('NE')