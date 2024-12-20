from functools import lru_cache

towels = []
designs = []
with open("input.txt") as f:
    line = f.readline().strip()
    data = line.split(", ")
    for i in data:
        towels.append(i)    

    for index, line in enumerate(f):
        if index > 0:
            designs.append(line.strip())

towels = set(towels)
@lru_cache(maxsize=None)
def check_design(design):
    if design in towels:
        return True
    
    for i in range(1, len(design)):
        if design[:i] in towels and check_design(design[i:]):
            return True
    return False

count_valid_design = 0
for design in designs:
    if check_design(design):
        count_valid_design += 1

print(count_valid_design)