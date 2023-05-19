import sys
input = sys.stdin.readline
from collections import Counter

name = list(map(str, input().strip()))
name.sort()

odd = Counter(name)

mid = ""

for i in name:
    if(odd[i] % 2 != 0):
        mid += i
        name.remove(i)

    if (len(mid) > 1):
        break

if (len(mid) > 1):
    print("I'm Sorry Hansoo")
else:
    E = ""

    # 반복문을 통해 팰린드롬을 반을 나누었을 때 왼쪽 부분을 더해준다.
    for i in range(0, len(name), 2):
        E += name[i]

    # 왼쪽 + 가운데(홀수) + 오른쪽
    print(E + mid + E[::-1])