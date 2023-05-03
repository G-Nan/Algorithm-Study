import sys

n, m = map(int, sys.stdin.readline().split())

voca_dict = {}

for _ in range(n):
    voca = sys.stdin.readline().strip()
    
    if len(voca) < m:
        continue
        
    if voca_dict.get(voca):
        voca_dict[voca][0] += 1
    else:
        voca_dict[voca] = [1, len(voca), voca]

answer = dict(sorted(voca_dict.items(), key = lambda x : (-x[1][0], -x[1][1], x[1][2])))

for word in answer:
    print(word)