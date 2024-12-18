
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
        print(move, robot_position)
        x, y = movements[move]
        if grid[robot_position[0]+x][robot_position[1]+y] == ".":
                print("First case")
                grid[robot_position[0]][robot_position[1]] = "."
                grid[robot_position[0]+x][robot_position[1]+y] = "@"
                robot_position = (robot_position[0]+x, robot_position[1]+y)
        elif grid[robot_position[0]+x][robot_position[1]+y] == "#":
            print("Second case")
            continue
        else:
            print("Third case")
            match move:
                case "^":
                    for i in range(robot_position[0], 0, -1):
                        if grid[i][robot_position[1]] == "#":
                            break
                        if grid[i][robot_position[1]] == ".":
                            to_be_checked = [(robot_position[0], robot_position[1])]
                            box_sx = []
                            box_dx = []
                            free_space = []
                            while to_be_checked:
                                print(to_be_checked)
                                position = to_be_checked.pop()
                                if grid[position[0]][position[1]] == "#":
                                    break
                                if grid[position[0]][position[1]] == ".":
                                    free_space.append(position)
                                    continue
                                if grid[position[0]+x][position[1]+y] == "[":
                                    to_be_checked.append((position[0]+x, position[1]+y))
                                    to_be_checked.append((position[0]+x, position[1]+y+1))
                                    box_sx.append((position[0]+x, position[1]+y))
                                elif grid[position[0]+x][position[1]+y] == "]":
                                    to_be_checked.append((position[0]+x, position[1]+y))
                                    to_be_checked.append((position[0]+x, position[1]-1))
                                    box_dx.append((position[0]+x, position[1]+y))
                            # find the element in box_sx that is the most on the left
                            left = sorted(box_sx, key=lambda x: x[1])[0]
                            right = sorted(box_dx, key=lambda x: x[1])[-1]
                            top = max(sorted(box_sx, key=lambda x: x[0])[0], sorted(box_dx, key=lambda x: x[0])[0])
                            free_space = [x for x in free_space if x[0] > top]
                            if len(free_space) == right[1] - left[1] - 1:
                                print("Found a free space")
                            # find the element in box_dx that is the most on the right

                        
                            

                # case "v":
                #     for i in range(robot_position[0], len(grid)-1):
                #         if grid[i][robot_position[1]] == "#":
                #             break
                #         if grid[i][robot_position[1]] == ".":
                #             grid[i][robot_position[1]] = "O"
                #             grid[robot_position[0]][robot_position[1]] = "."
                #             grid[robot_position[0]+x][robot_position[1]+y] = "@"
                #             robot_position = (robot_position[0]+x, robot_position[1]+y)

                #             break
                case "<":
                    for i in range(robot_position[1], 0, -1):
                        if grid[robot_position[0]][i] == "#":
                            break
                        if grid[robot_position[0]][i] == ".":
                            grid[robot_position[0]].insert(robot_position[1]+1, ".")
                            grid[robot_position[0]].pop(i)
                            robot_position = (robot_position[0]+x, robot_position[1]+y)
                            break
                case ">":
                    for i in range(robot_position[1], len(grid[0])-1):
                        if grid[robot_position[0]][i] == "#":
                            break
                        if grid[robot_position[0]][i] == ".":
                            grid[robot_position[0]].pop(i)
                            grid[robot_position[0]].insert(robot_position[1]-1, ".")
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
        new_line = []
        for char in line.strip():
            if char == "#":
                new_line.append("#")
                new_line.append("#")
            elif char == ".":
                new_line.append(".")
                new_line.append(".")
            elif char == "@":
                new_line.append("@")
                new_line.append(".")
            elif char == "O":
                new_line.append("[")
                new_line.append("]")
        grid.append(new_line)
        # grid.append(list(line.strip()))
        if "@" in new_line:
            robot_position = (index, new_line.index("@"))
        
    for line in lines[index+1:]:
        moves.extend(line.strip())

for line in grid:
    print("".join(line))

grid = move_robot(grid, robot_position, moves)

for line in grid:
    print("".join(line))

# result = 0
# for line_index, line in enumerate(grid):
#     for column_index, char in enumerate(line):
#         if char == "O":
#             result +=  line_index * 100 + column_index  

# print(result)