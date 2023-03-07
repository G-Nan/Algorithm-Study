size = list(map(int, input().split()))
mat = []
for i in range(2 * size[0]):
    element = list(map(int, input().split()))
    mat.append(element)
    
mat1 = mat[:size[0]]
mat2 = mat[size[0]:]

for i in range(size[0]):
    for x, y in zip(mat1[i], mat2[i]):
        print(x + y, end = ' ')
    print('')