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
    # print("Design: ", design)
    if design in towels:
        tmp = 1
        for i in range(1, len(design)):
            if design[:i] in towels:
                tmp += check_design(design[i:])
        return tmp

    count = 0
    for i in range(1, len(design)):
        # print("evaluating: ", design)
        if design[:i] in towels:
            # print("OK: ", design[:i], count, "Calling on ", design[i:])

            count += check_design(design[i:])
        # else:
        #     print("NO: ", design[:i])
    return count

cache = {}
count_valid_design = 0
for design in designs:
    tmp = check_design(design)
    count_valid_design += tmp
    # print(design, tmp)

print(count_valid_design)