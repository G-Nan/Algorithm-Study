def solution(m, n, startX, startY, balls):
    answer = []
    loc = []


    for ball in balls:
        a, b, c, d = startX, startY, ball[0], ball[1]
        left = (a+c)**2+(b-d)**2
        right = (2*m-(a+c))**2+(b-d)**2
        bottom = (a-c)**2+(b+d)**2
        top = (a-c)**2+(2*n-(b+d))**2
        dis = [left, right, bottom, top]
        
        if startX == ball[0]:
            if startY > ball[1]:
                del dis[2]
            elif startY < ball[1]:
                del dis[3]
        elif startY == ball[1]:
            if startX > ball[0]:
                del dis[0]
            elif startX < ball[0]:
                del dis[1]
        
        answer.append(min(dis))
    return answer


