rows = int(input())
column = int(input())

Matrix  = [[None for i in range(column)] for j in range(rows)]

for i in range(rows):
    for j in range(column):
        Matrix[i][j] = int(input())

row_sum = []
col_sum = []

for i in range(rows):
    sum = 0
    for  j in range(column):
        sum += Matrix[i][j]
    row_sum.append(sum)
for i in range(rows):
    sum = 0
    for j in range(column):
        sum+=Matrix[j][i]
    col_sum.append(sum)

print(row_sum)
print(col_sum)
