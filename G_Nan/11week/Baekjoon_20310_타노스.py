s = input()

c_0 = s.count('0')
c_1 = s.count('1')

answer = s.replace('1', '', int(c_1/2))
answer = answer[::-1].replace('0', '', int(c_0/2))[::-1]
print(answer)