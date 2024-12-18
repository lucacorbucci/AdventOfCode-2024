

def find_trailhead(grid):
    trailheads = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 9:
                trailheads.append((i, j))

    return trailheads

def check_bound(position, grid):
    if position[0] < 0 or position[0] >= len(grid):
        return False 
    if position[1] < 0 or position[1] >= len(grid[0]):
        return False 
    return True

def find_paths(grid, position):
    dd = []
    def dfs(position, next_value):
        if grid[position[0]][position[1]] != next_value:
            return False
        if next_value == 0 and grid[position[0]][position[1]] == 0:
            dd.append(position)
            return True
        
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        neighbors = [(position[0] + move[0], position[1] + move[1]) for move in moves]
        neighbors = [neighbor for neighbor in neighbors if check_bound(neighbor, grid)]
        max_path = []
        for neighbor in neighbors:
            path = dfs(neighbor, next_value - 1)
        
        return path
        

    count = dfs(position, 9)
    return len(dd)

grid = None 

with open("input.txt") as file:
    grid = [[int(char) for char in line.strip()] for line in file]

trailheads = find_trailhead(grid)
all_paths = []
for trailhead in trailheads:
    all_paths.append(find_paths(grid, trailhead))

print(all_paths)
print(sum(all_paths))