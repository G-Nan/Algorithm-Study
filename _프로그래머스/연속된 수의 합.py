def solution(num, total):
    answer = []
    Avg = total // num
    for i in range(Avg - (num-1)//2, (Avg + (num+2)//2)):
        answer.append(i)
    return answer

print(solution(5, 15))