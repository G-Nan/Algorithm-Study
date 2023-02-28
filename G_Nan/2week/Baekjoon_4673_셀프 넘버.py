unit = []
a = 0

while a <= 10000:
    value = 0
    b = []
    for i in range(len(str(a))):
        b.append(int(str(a)[i]))
    value += a + sum(b)
    unit.append(value)
    a += 1
unit = set(unit)

for i in range(1, 10001):
    if i not in unit:
        print(i)