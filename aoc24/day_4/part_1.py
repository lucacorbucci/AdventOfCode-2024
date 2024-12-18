import os 
import time
from aoc24.utils.matrix import Matrix

lines = []
with open('input.txt') as f:
    for line in f:
        lines.append(list(line.strip()))

result = 0
matrix = Matrix(lines)
all_rows = matrix.get_all_rows()
all_rows_reverse = [row[::-1] for row in all_rows]
all_columns = matrix.get_all_columns()
all_columns_reverse = [column[::-1] for column in all_columns]
all_diagonals = matrix.get_all_diagonals()
all_diagonals_reverse = [diagonal[::-1] for diagonal in all_diagonals]

all_combinations = all_rows + all_rows_reverse + all_columns + all_columns_reverse + all_diagonals + all_diagonals_reverse

word = "XMAS"
for combination in all_combinations:
    result += "".join(combination).count(word)

print(result)