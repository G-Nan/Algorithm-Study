n = int(input())

words = [input() for _ in range(n)]

example = words[0]
answer = 0

a_list = list(example)

for word in words[1:]:
    a = a_list.copy()
    k = 0
    for alp in word:
        if alp in a:
            a.remove(alp)
        else:
            k += 1
            
    if k > 1:
        continue
    
    if len(a) <= 1:
        answer += 1
    
print(answer)