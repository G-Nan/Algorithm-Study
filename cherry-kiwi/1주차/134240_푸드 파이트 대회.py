def solution(food):
    foods=''
    for i in range(1,len(food)): #물 제외해야하니까 1부터 food배열 -1 까지
        foods+=str(i)*(food[i]//2) #str(i)를 (food[i]//2)번 반복
    foods_reversed=''.join(reversed(list(foods)))
    return foods+'0'+foods_reversed