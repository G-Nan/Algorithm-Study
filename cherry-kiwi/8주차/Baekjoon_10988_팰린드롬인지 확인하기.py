#팰린드롬 = 기러기
word=list(str(input()))

if word == list(reversed(word)):
    print(1)
if word != list(reversed(word)):
    print(0)