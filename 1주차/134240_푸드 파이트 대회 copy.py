def solution(food):
    answer = []
    j = 0
    for i in food:
        j += 1
        
        if(i % 2 == 1):
            v = i - 1
            v = v // 2
            
        elif(i % 2 == 0):
            v = i // 2
            
        for _ in range(v):
            answer.append(j-1)
            
    R = list(reversed(answer))
    answer.append(0)
    answer.extend(R)
    
    return "".join(map(str, answer))