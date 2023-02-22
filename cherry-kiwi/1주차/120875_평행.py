def solution(dots):
    dots=sorted(dots)
    x=[dot[0] for dot in dots] #x에 dots배열의 첫번째 요소 담음
    y=[dot[1] for dot in dots] #y에 dots배열의 두번째 요소 담음
    line1=(y[3]-y[2])/(x[3]-x[2])
    line2=(y[1]-y[0])/(x[1]-x[0])
    
    if line1==line2:
        return 1
    else: return 0