m,n = map(int,input().split())
matrix_1 = [list(map(int,input().split())) for i in range(m)]
matrix_2 = [list(map(int,input().split())) for i in range(m)]
print(matrix_1)
print(matrix_2)
result = []
for i in range(m):
    l =[]
    for j in range(n):
        l = l+ [0]
    result.append(l)
#     print(l)
print(result)
for i in range(m):
    for j in range(m):
       result[i][j] = matrix_1[i][j] + matrix_2[i][j]
print(result)
