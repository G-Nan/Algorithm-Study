a = int(input())
matters = [input() for _ in range(a)]

alp = 'abcdefghijklmnopqrstuvwxyz'
num = []

for matter in matters:
    for j in alp:
        matter = matter.replace(j, ' ')
    matter = ' '.join(matter.split())
    num += matter.split()

num = list(map(int, num))
num.sort()
print(*num, sep = '\n')