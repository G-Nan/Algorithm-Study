import math

A, B, V = map(int, input().split( ))
answer = 0

V -= A
answer += 1

up = A - B
answer += math.ceil(V / up)

print(answer)