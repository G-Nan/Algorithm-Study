str1 = input()
qt = len(str1)//2
if str1[:qt] == str1[:-1 * qt -1:-1]:
    print('1')
else:
    print('0')