rows = 3
columns = 3
matrix = [[None for i in range(columns)] for i in range(rows)]
print(matrix)

for i in range(rows):
    for j in range(columns):
        matrix[i][j] = int(input())
print(matrix)

# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]