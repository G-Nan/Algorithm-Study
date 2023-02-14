def solution(s, skip, index):
    apb = 'abcdefghijklmnopqrstuvwxyz'
    
    for i in skip:
        apb = apb.replace(i, '')
    
    answer = ''
    
    for i in s:
        answer += apb[(apb.index(i) + index)%len(apb)] 
        
    return answer