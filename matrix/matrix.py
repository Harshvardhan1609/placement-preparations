rows = int(input())
column = int(input())

Matrix  = [[None for i in range(column)] for j in range(rows)]

for i in range(rows):
    for j in range(column):
        Matrix[i][j] = int(input())

print(Matrix)

#Columns

rows = int(input())
column = int(input())

Matrix  = [[None for i in range(column)] for j in range(rows)]

for i in range(rows):
    for j in range(column):
        Matrix[j][i] = int(input())

print(Matrix)
