import os 
import time
from aoc24.utils.matrix import Matrix

lines = []
with open('input.txt') as f:
    for line in f:
        lines.append(list(line.strip()))

result = 0
matrix = Matrix(lines)

for i, row in enumerate(matrix.matrix):
    for j, column in enumerate(row):
        if matrix.matrix[i][j] == "A":
            if (i - 1 >= 0 and j - 1 >= 0) and (i + 1 < matrix.rows and j - 1 >= 0) and (i - 1 >= 0 and j + 1 < matrix.columns) and (i + 1 < matrix.rows and j + 1 < matrix.columns):
                diagonal_1 = matrix.matrix[i - 1][j - 1] + matrix.matrix[i][j] + matrix.matrix[i + 1][j + 1]
                diagonal_2 = matrix.matrix[i + 1][j - 1] + matrix.matrix[i][j] + matrix.matrix[i - 1][j + 1]
                if (diagonal_1 == "MAS" or diagonal_1 == "SAM") and (diagonal_2 == "MAS" or diagonal_2 == "SAM"):
                    result += 1
print(result)
