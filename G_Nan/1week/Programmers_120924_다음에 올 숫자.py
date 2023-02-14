def solution(common):
    answer = 0
    
    if common[0] + common[2] == 2 * common[1]:
        answer = common[0] + (common[1]-common[0])*len(common)
    else:
        answer = common[0] * (common[1]/common[0])**len(common)
    return answer