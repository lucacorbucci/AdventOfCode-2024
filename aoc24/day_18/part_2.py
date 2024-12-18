from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder
import copy
import sys
sys.setrecursionlimit(15000)

def compute_path(grid, start, end):
    """
    Compute the path from start to end in the grid

    Returns the path and the number of operations
    """
    new_grid = []
    for line in grid:
        line = [0 if char=="#" else 1 for char in line]
        new_grid.append(list(line))


    new_grid = Grid(matrix=new_grid)
    start = new_grid.node(start[1], start[0])
    end = new_grid.node(end[1], end[0])
    finder = DijkstraFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, new_grid)

    return path, len(path)-1


start = (0, 0)
end = (70, 70)
grid = [["." for _ in range(71)] for _ in range(71)]
bytes_list = []
with open('input.txt') as f:
    for index, line in enumerate(f):
        x = line.split(",")[0]
        y = line.split(",")[1]
        
        if index <= 1024:
            grid[int(y)][int(x)] = "#"
        else:
            bytes_list.append((int(x), int(y)))

def search_byte(sx, dx):
    """
    Search for the byte that makes the path from start 
    to end impossible by using a binary search.
    """
    global grid
    if sx == dx:
        return f"{bytes_list[sx][0]},{bytes_list[sx][1]}"

    mid = (sx+dx)//2
    new_grid = copy.deepcopy(grid)
    for i in range(mid+1):
        x, y = bytes_list[i]
        new_grid[y][x] = "#"
    path, length = compute_path(new_grid, start, end) 
    if length == -1:
        return search_byte(sx, mid)
    else:
        return search_byte(mid+1, dx)

print(search_byte(0, len(bytes_list)))