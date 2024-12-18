
def check_bound(position, grid):
    if position[0] < 1 or position[0] >= len(grid)-1:
        return False 
    if position[1] < 1 or position[1] >= len(grid[0])-1:
        return False 
    return True

# def search_free_space

movements = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}

def move_robot(grid, robot_position, moves):
    for move in moves:
        x, y = movements[move]
        if grid[robot_position[0]+x][robot_position[1]+y] == ".":
                grid[robot_position[0]][robot_position[1]] = "."
                grid[robot_position[0]+x][robot_position[1]+y] = "@"
                robot_position = (robot_position[0]+x, robot_position[1]+y)
        elif grid[robot_position[0]+x][robot_position[1]+y] == "#":
            continue
        else:
            match move:
                case "^":
                    for i in range(robot_position[0], 0, -1):
                        if grid[i][robot_position[1]] == "#":
                            break
                        if grid[i][robot_position[1]] == ".":
                            grid[i][robot_position[1]] = "O"
                            grid[robot_position[0]][robot_position[1]] = "."
                            grid[robot_position[0]+x][robot_position[1]+y] = "@"
                            robot_position = (robot_position[0]+x, robot_position[1]+y)

                            break
                case "v":
                    for i in range(robot_position[0], len(grid)-1):
                        if grid[i][robot_position[1]] == "#":
                            break
                        if grid[i][robot_position[1]] == ".":
                            grid[i][robot_position[1]] = "O"
                            grid[robot_position[0]][robot_position[1]] = "."
                            grid[robot_position[0]+x][robot_position[1]+y] = "@"
                            robot_position = (robot_position[0]+x, robot_position[1]+y)

                            break
                case "<":
                    for i in range(robot_position[1], 0, -1):
                        if grid[robot_position[0]][i] == "#":
                            break
                        if grid[robot_position[0]][i] == ".":
                            grid[robot_position[0]][i] = "O"
                            grid[robot_position[0]][robot_position[1]] = "."
                            grid[robot_position[0]+x][robot_position[1]+y] = "@"
                            robot_position = (robot_position[0]+x, robot_position[1]+y)
                            break
                case ">":
                    for i in range(robot_position[1], len(grid[0])-1):
                        if grid[robot_position[0]][i] == "#":
                            break
                        if grid[robot_position[0]][i] == ".":
                            grid[robot_position[0]][i] = "O"
                            grid[robot_position[0]][robot_position[1]] = "."
                            grid[robot_position[0]+x][robot_position[1]+y] = "@"
                            robot_position = (robot_position[0]+x, robot_position[1]+y)

                            break
    return grid
                 

grid = []
robot_position = None
moves = []
with open("input.txt") as file:
    lines = file.readlines()
    for index, line in enumerate(lines):
        if line == "\n":
            break
        
        grid.append(list(line.strip()))
        if "@" in line:
            robot_position = (index, line.index("@"))
        
    for line in lines[index+1:]:
        moves.extend(line.strip())

grid = move_robot(grid, robot_position, moves)

result = 0
for line_index, line in enumerate(grid):
    for column_index, char in enumerate(line):
        if char == "O":
            result +=  line_index * 100 + column_index  

print(result)