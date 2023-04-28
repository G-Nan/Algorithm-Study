from string import ascii_lowercase
alphabet_list = list(ascii_lowercase)

s=list(str(input())) #알파벳 배열
for i in range(len(alphabet_list)):
    s2=s.count(alphabet_list[i])
    print(s2, end=' ')