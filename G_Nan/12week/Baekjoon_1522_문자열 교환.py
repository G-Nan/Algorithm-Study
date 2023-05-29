s = input()

a = s.count('a')
b = len(s) - a

ab1 = 'a'*a + 'b'*b
min_k = len(ab1)

for i in range(len(ab1)):
    ab1 = ab1[1:] + ab1[0]
    
    k = 0
    
    for i in range(len(ab1)):
        if ab1[i] != s[i]:
            k += 1
    min_k = min(min_k, k)
    
print(int(min_k/2))