n = int(input())
target = list(input()) # 비교 대상 단어(첫 단어)
answer = 0
count = 0

for _ in range(n-1):
    compare = target[:] 
    word = input() # 새로운 단어

    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            count += 1

    if cnt < 2 and len(compare) < 2:
        answer += 1

print(answer)