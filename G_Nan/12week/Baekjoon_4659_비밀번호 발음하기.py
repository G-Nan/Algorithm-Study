V = ['a', 'e', 'i', 'o', 'u']

while True:
    
    pw = input()
    v = 0
    c = 0
    
    if pw == 'end':
        break

    for i in range(len(pw)):
    
        if pw[i] in V:
            v += 1
            c = 0
        else:
            v = 0
            c += 1
    
        if v >= 3 or c >= 3 or c == len(pw):
            print(f'<{pw}> is not acceptable.')
            break
    
        if i >= 1:
            if (pw[i] == pw[i-1]) and (pw[i] not in ['e', 'o']):
                print(f'<{pw}> is not acceptable.')
                break
        
        if i == len(pw)-1:
            print(f'<{pw}> is acceptable.')