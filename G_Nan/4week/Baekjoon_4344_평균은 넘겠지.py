x0 = int(input())
x = [list(map(int, input().split( ))) for _ in range(x0)]

for i in x:
    k = 0
    mean = sum(i[1:])/i[0]
    for j in i[1:]:
        if j > mean:
            k += 1
    smart = (k/i[0])*100
    print('%0.3f' %smart  + '%')