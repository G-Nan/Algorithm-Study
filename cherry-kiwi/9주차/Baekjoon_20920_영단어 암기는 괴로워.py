import sys
input = sys.stdin.readline

n, m=map(int, input().rsplit().split()) #개행문자(\n) x 
words=[] #외울 단어들
result=[]

for i in range(n):
    word=input()
    if len(word)>=m:
        words.append(word)

print(words)