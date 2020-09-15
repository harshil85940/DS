#addition
mat1 = [[1, 2], [3, 4]]
mat2 = [[1, 2], [3, 4]]
mat3 = [[0, 0], [0, 0]]

for i in range(0, 2):
    for j in range(0, 2):
        mat3[i][j] = mat1[i][j] + mat2[i][j]

for i in range(0, 2):
    for j in range(0, 2):
        print(mat3[i][j], end="")
print()

#multiplication
mat1 = [[10, 9], [8, 6]]
mat2 = [[1, 2], [3, 4]]
mat3 = [[0, 0], [0, 0]]

for i in range(0, 2):
    for j in range(0, 2):
        mat3[i][j] = mat1[i][j] * mat2[i][j]


for i in range(len(mat1)):
    for j in range(len(mat2[0])):
        for k in range(len(mat2)):
            mat3[i][j] =mat3[i][j] + ( mat1[i][k] * mat2[k][j])


for r in mat3:
    print(r)
    
 #transpose
 X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)
