num = int(input())
players = [input() for _ in range(num)]

answer = ''
firstnames = []

for i in players:
    firstnames.append(i[0])
    if firstnames.count(i[0]) >= 5:
        answer += i[0]
        
if len(answer) > 0:
    answer = ''.join(sorted(set(answer), reverse = False))
    print(answer)
else:
    print('PREDAJA')