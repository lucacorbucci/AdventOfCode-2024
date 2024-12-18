from collections import defaultdict


def check_bound(position, grid):
    if position[0] < 0 or position[0] >= len(grid):
        return False 
    if position[1] < 0 or position[1] >= len(grid[0]):
        return False 
    return True

def get_neighbours(position, grid):
    neighbours = []
    # get only the 4 neighbours UP, DOWN, LEFT, RIGHT
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if i == 0 or j == 0:
                neighbours.append((position[0] + i, position[1] + j))
    return neighbours

def process(grid, position):
    while True: 
        if not position in visited:
            visited.add(position)
            neigh = get_neighbours(position, garden)
            valid_neigh = []
            tmp[(position[0], position[1])] = 0
            for n in neigh:
                
                if not check_bound(n, garden):
                    tmp[(position[0], position[1])] += 1
                elif garden[n[0]][n[1]] != grid[position[0]][position[1]]:
                    tmp[(position[0], position[1])] += 1
                elif check_bound(n, garden) and not n in visited and garden[n[0]][n[1]] == grid[position[0]][position[1]]:
                    valid_neigh.append(n)
            for n in valid_neigh:
                process(grid, n)
            if len(valid_neigh) == 0:
                break
        else:
            break
    


garden = [] 
with open("input.txt") as f:
    garden = f.readlines()
    garden = [list(x.strip()) for x in garden]


position = (0, 0)
visited = set()

all_position = []
for i in range(len(garden)):
    for j in range(len(garden[0])):
        all_position.append((i, j))

result = 0
for position in all_position: 
    tmp = defaultdict(int)
    process(garden, position)
    perimetro = 0
    for k, v in tmp.items():
        perimetro += v
    result += perimetro * len(tmp)

print(result)

# plants = set()
# for line in garden:
#     for plant in line:
#         plants.add(plant)
# print(plants)


# for plant in plants:
#     filtered_garden = []
#     for line in garden:
#         tmp = []
#         for position in line: 
#             if position == plant:
#                 tmp.append(str(plant))
#             else:
#                 tmp.append(".")
#         filtered_garden.append(tmp)

