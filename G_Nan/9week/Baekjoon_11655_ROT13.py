str1 = input()

alp = 'abcdefghijklmnopqrstuvwxyz'
code = ''

for i in str1:
    if i.isupper():
        code += alp[(alp.index(i.lower()) + 13)%len(alp)].upper()
    elif i.islower():
        code += alp[(alp.index(i) + 13)%len(alp)]
    else:
        code += i
       
print(code)