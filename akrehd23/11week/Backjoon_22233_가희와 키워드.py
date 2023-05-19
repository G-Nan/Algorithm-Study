import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = dict()
for _ in range(n) :
    board[input().rstrip()] = 1
    
for _ in range(m) :
    tmp = sorted(input().rstrip().split(','))
    
    for t in tmp :
        if t in board.keys() :
            if board[t] == 1 :
                board[t] -= 1
                n -= 1
    print(n)