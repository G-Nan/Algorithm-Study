def solution(dots):
    answer = 0
    
    a1 = dots[0]
    dots.remove(a1)
    
    for i in range(len(dots)):
        a2 = dots[i]
        b1 = dots[(i+1)%len(dots)]
        b2 = dots[(i+2)%len(dots)]
        
        grad1 = (a1[1]-a2[1])/(a1[0]-a2[0])
        grad2 = (b1[1]-b2[1])/(b1[0]-b2[0])
        if grad1 == grad2:
            answer = 1
            
    return answer