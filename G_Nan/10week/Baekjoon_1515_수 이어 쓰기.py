a = input()
b = 0

while len(a) != 0:
    b += 1
    for i in list(str(b)):
        
        if (i == a[0]):
            if len(a) == 1:
                a = ''
                break
            else:
                a = a[1:]

    b = int(b)
    
print(b)