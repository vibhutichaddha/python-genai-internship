matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]
row_sums = []
for row in matrix:
    row_sums.append(sum(row))
column_sums = []
for col in range(len(matrix[0])):
    column_sum = 0
    for row in matrix:
        column_sum += row[col]
    column_sums.append(column_sum)
transpose = []
for col in range(len(matrix[0])):
    row = []
    for i in range (len(matrix)):
        row.append(matrix[i][col])
    transpose.append(row)
print("Row sums:", row_sums)
print("Column sums:", column_sums)
print("Transpose of the matrix:",transpose)