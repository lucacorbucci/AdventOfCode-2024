def check_tree(grid):
    tree = False
    position = None
    counter = 0
    for index, line in enumerate(grid):
        l = "".join(map(str, line))
        
        if "111" in l:
            position = l.index("111")
            if index + 2 < len(grid):
                next_line = "".join(map(str, grid[index + 1]))
                next_line_2 = "".join(map(str, grid[index + 2]))
                if "111" in next_line[position:position + 3] and "111" in next_line_2[position:position + 3]:
                    return True
            
            # counter = 1
            # print("Found 111 ", counter, position)

    
    # return False
    # check if all the items in the grid are 0 or 1:
    # for line in grid:
    #     for item in line:
    #         if item > 1:
    #             return False
    # return True


wide = 101
tall = 103
# seconds = 100

grid = [[0 for i in range(wide)] for j in range(tall)]

positions = []
moves = []

with open("input.txt") as file:
    lines = file.readlines()
    for line in lines: 
        line = line.strip()
        p = eval(line.split(" ")[0].split("=")[1])
        v = eval(line.split(" ")[1].split("=")[1])
        positions.append(p)
        moves.append(v)
    second = 0
    # for second in range(seconds):
    while True:
        second += 1
        for index, position in enumerate(positions):
            
            if grid[position[1]][position[0]] > 0:
                grid[position[1]][position[0]] -= 1
            
            # the first number is the x, the second is the y
            total_v_x = position[0] + moves[index][0]
            total_v_y = position[1] + moves[index][1]

            final_x = total_v_x % wide
            final_y = total_v_y % tall

            if final_x < 0:
                final_x = wide + final_x
            if final_y < 0:
                final_y = tall + final_y
            
            grid[final_y][final_x] += 1


            positions[index] = [final_x, final_y]

        # for i in range(tall):
        #     print(grid[i])
        # print("\n\n")
        if check_tree(grid):
            for i in range(tall):
                print("".join(map(str, grid[i])))
            print("Seconds: ", second)
            
            break
    