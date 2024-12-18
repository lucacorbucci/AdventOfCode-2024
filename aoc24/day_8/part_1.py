from itertools import combinations

# position[0] is the x coordinate
# position[1] is the y coordinate
def check_bound(position, grid):
    if position[1] < 0 or position[1] >= len(grid):
        return False 
    if position[0] < 0 or position[0] >= len(grid[0]):
        return False 
    return True


def manhattan_distance(pos_1, pos_2):
    return abs(pos_1[0] - pos_2[0]) + abs(pos_1[1] - pos_2[1])




antinodes = []
antennas = {}
grid = []
with open('input.txt') as f:
    for line in f:
        grid.append(list(line.strip()))
        antinodes.append(["."]*len(line.strip()))
    
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char != ".":
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((y, x))

to_remove = []
for antenna, occurrences in antennas.items():
    if len(occurrences) < 2:
        to_remove.append(antenna)

for antenna in to_remove:
    antennas.pop(antenna)

result = 0
print(antennas.items())
# generate all the combinations of antennas
for key, value in antennas.items():
    groups = list(combinations(value, 2))
    result += len(value)
    print(result, len(value))
    print(value)
    for group in groups:
        horizontal_distance = abs(group[0][1] - group[1][1])
        vertical_distance = abs(group[0][0] - group[1][0])
        

        left = group[0] if group[0][1] < group[1][1] else group[1]
        right = group[0] if group[0][1] > group[1][1] else group[1]
        top = group[0] if group[0][0] < group[1][0] else group[1]
        down = group[0] if group[0][0] > group[1][0] else group[1]

        if left == top and right == down:
            if check_bound((top[0]-vertical_distance, top[1]-horizontal_distance), grid):
                antinodes[top[0]-vertical_distance][top[1]-horizontal_distance] = "#"
                i = 2
                while True:
                    if check_bound((top[0]-i*vertical_distance, top[1]-i*horizontal_distance), grid):
                        if antinodes[top[0]-i*vertical_distance][top[1]-i*horizontal_distance] == ".":
                            antinodes[top[0]-i*vertical_distance][top[1]-i*horizontal_distance] = "#"
                        i += 1
                    else:
                        break
            if check_bound((down[0]+vertical_distance, down[1]+horizontal_distance), grid):
                antinodes[down[0]+vertical_distance][down[1]+horizontal_distance] = "#"
                i = 2
                while True:
                    if check_bound((down[0]+i*vertical_distance, down[1]+i*horizontal_distance), grid):
                        if antinodes[down[0]+i*vertical_distance][down[1]+i*horizontal_distance] == ".":
                            antinodes[down[0]+i*vertical_distance][down[1]+i*horizontal_distance] = "#"
                        i += 1
                    else:
                        break
        elif left == down and right == top:
            if check_bound((down[0]+vertical_distance, down[1]-horizontal_distance), grid):
                antinodes[down[0]+vertical_distance][down[1]-horizontal_distance] = "#"
                i = 2
                while True:
                    if check_bound((down[0]+i*vertical_distance, down[1]-i*horizontal_distance), grid):
                        if antinodes[down[0]+i*vertical_distance][down[1]-i*horizontal_distance] == ".":
                            antinodes[down[0]+i*vertical_distance][down[1]-i*horizontal_distance] = "#"
                        i += 1
                    else:
                        break
            if check_bound((top[0]-vertical_distance, top[1]+horizontal_distance), grid):
                antinodes[top[0]-vertical_distance][top[1]+horizontal_distance] = "#"
                i = 2
                while True:
                    if check_bound((top[0]-i*vertical_distance, top[1]+i*horizontal_distance), grid):
                        if antinodes[top[0]-i*vertical_distance][top[1]+i*horizontal_distance] == ".":
                            antinodes[top[0]-i*vertical_distance][top[1]+i*horizontal_distance] = "#"
                        i += 1
                    else:
                        break
        
for y, line in enumerate(antinodes):
    for x, char in enumerate(line):
        if grid[y][x] == "." and char == "#":
            grid[y][x] = antinodes[y][x]
            result += 1

for line in grid: 
    print("".join(line))

print(result)