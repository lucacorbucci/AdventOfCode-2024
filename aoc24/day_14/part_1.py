

wide = 101
tall = 103
seconds = 100

grid = [[0 for i in range(wide)] for j in range(tall)]

with open("input.txt") as file:
    lines = file.readlines()
    for line in lines: 
        line = line.strip()
        p = eval(line.split(" ")[0].split("=")[1])
        v = eval(line.split(" ")[1].split("=")[1])
        print("p: ", p)

        # the first number is the x, the second is the y
        total_v_x = p[0] + v[0]*seconds
        total_v_y = p[1] + v[1]*seconds

        final_x = total_v_x % wide
        final_y = total_v_y % tall

        if final_x < 0:
            final_x = wide + final_x
        if final_y < 0:
            final_y = tall + final_y
        
        grid[final_y][final_x] += 1

mid_w = wide // 2
mid_t = tall // 2
print(mid_w, mid_t)
grid[mid_t] = [0]*len(grid[mid_t])
for i in range(tall):
    grid[i][mid_w] = 0

# print the grid 
for i in range(tall):
    print(grid[i])

# count the numbers that are not zero in each quadrant
count_1 = 0
for i in range(0, mid_w):
    for j in range(0, mid_t):
        if grid[j][i] != 0:
            count_1 += grid[j][i]

count_2 = 0
for i in range(mid_w, wide):
    for j in range(0, mid_t):
        if grid[j][i] != 0:
            count_2 += grid[j][i]

count_3 = 0
for i in range(0, mid_w):
    for j in range(mid_t, tall):
        if grid[j][i] != 0:
            count_3 += grid[j][i]
    
count_4 = 0
for i in range(mid_w, wide):
    for j in range(mid_t, tall):
        if grid[j][i] != 0:
            count_4 += grid[j][i]

print(count_1, count_2, count_3, count_4)
print(count_1*count_2*count_3*count_4)