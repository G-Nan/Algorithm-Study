a, b, v=map(int, input().split())

i=1
while True:
    if a>v: 
        print(1)
        break
    elif a*2-b>v:
        print(2)
        break
    elif a*(i+1)-b*i>v:
        print(i)
        break
    else:
        i+=1

#시간초과