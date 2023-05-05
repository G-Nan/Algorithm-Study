s=input()

for i in s:
    if 65<=ord(i)<=77 or 97<=ord(i)<=109: #A~M or a~m
        print(chr(ord(i)+13), end='')
    elif 78<=ord(i)<=90 or 110<=ord(i)<=122: #N~Z or n~z
        print(chr(ord(i)-13), end='')
    else:
        print(i, end='')