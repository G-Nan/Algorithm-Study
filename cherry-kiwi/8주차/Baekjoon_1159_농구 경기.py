n=int(str(input()))
players=[]
first_name=[]
result=[]

for _ in range(n):
    first=input()
    players.append(first[0])

first_name=set(players)

for i in first_name:
    if players.count(i)>=5:
        result.append(i)

if len(result)>0:
    print(''.join(sorted(result)))
else:
    print("PREDAJA")