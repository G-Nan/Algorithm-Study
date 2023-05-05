import re

n=int(input())
string=re.compile("[0-9]+") #숫자만
new_string=[]

for i in range(n):
    strings = string.findall(input()) #패턴찾기
    for j in strings:
        new_string.append(int(j))

new_string.sort()
for k in range(len(new_string)):
    print(new_string[k])