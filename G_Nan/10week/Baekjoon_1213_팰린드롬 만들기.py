name = list(input())

answer = ''
a = sorted(list(set(name.copy())))

k = 0   # 개수가 홀수인 알파벳의 개수
for i in a:
    if name.count(i)%2 == 1:
        k += 1

l = ''  # 개수가 홀수인 알파벳
for i in a:
    if name.count(i)%2 == 0:
        answer += i*int(name.count(i)/2)
    else:
        answer += i*int(name.count(i)//2)
        l = i

if k == 0:
    answer += answer[::-1]
elif k == 1:
    answer += l
    answer += answer[-2::-1]
elif k > 1:
    answer = "I'm Sorry Hansoo"

print(answer)