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
            for n, direction in zip(neigh, ["UP", "LEFT", "RIGHT", "DOWN"]):
                
                if not check_bound(n, garden):
                    tmp[(position[0], position[1])] += 1
                    if direction not in tmp_2:
                        tmp_2[direction] = []
                    tmp_2[direction].append(n)

                elif garden[n[0]][n[1]] != grid[position[0]][position[1]]:
                    tmp[(position[0], position[1])] += 1
                    if direction not in tmp_2:
                        tmp_2[direction] = []
                    tmp_2[direction].append(n)

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
    if position not in visited:
        tmp = defaultdict(int)
        tmp_2 = {}
        process(garden, position)
        perimetro = 0
        # for k, v in tmp.items():
        #     perimetro += v
        for direction in ["UP", "DOWN"]:
            if direction in tmp_2:
                moves = tmp_2[direction]
                moves = sorted(moves, key=lambda x: (x[0], x[1]))
                perimetro += 1
                prev = moves[0]
                for move in moves[1:]:
                    
                    if move[0] != prev[0] or move[1] != prev[1]+1:
                        perimetro += 1
                    if direction == "DOWN":
                        print(move, prev, perimetro)
                    prev = move
                print(direction, moves, " current perimeter: ", perimetro)
        
        for direction in ["RIGHT", "LEFT"]:
            if direction in tmp_2:
                moves = tmp_2[direction]
                moves = sorted(moves, key=lambda x: (x[1], x[0]))

                perimetro += 1
                prev = moves[0]
                for move in moves[1:]:
                    
                    if move[1] != prev[1] or move[0] != prev[0] + 1:
                        perimetro += 1
                    prev = move
                print(direction, moves, " current perimeter: ", perimetro)
                
        if perimetro > 0:
            print(perimetro, len(tmp))
        result += perimetro * len(tmp)

print(result)
