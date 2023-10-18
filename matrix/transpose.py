rows = int(input())
column = int(input())

Matrix  = [[None for i in range(column)] for j in range(rows)]

for i in range(rows):
    for j in range(column):
        Matrix[i][j] = int(input())

print(Matrix)

for i in range(rows):
    for j in range(column):
        Matrix[i][j] = Matrix[j][i]

print(Matrix)
