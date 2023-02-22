def solution(food):
    answer = ''
    
    k = 0
    eat = ''
    for i in food: 
        if k == 0:
            pass
        
        eat += str(k) * (i // 2)
        k += 1
    
    answer = eat + '0' + eat[::-1]
    return answer