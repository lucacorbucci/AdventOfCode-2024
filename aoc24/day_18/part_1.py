from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder


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

    print(new_grid.grid_str(path=path, start=start, end=end))
    return path, len(path)-1



grid = [["." for _ in range(71)] for _ in range(71)]
print(grid)
with open('input.txt') as f:
    for index, line in enumerate(f):
        x = line.split(",")[0]
        y = line.split(",")[1]
        grid[int(y)][int(x)] = "#"
        if index == 1024:
            break

start = (0, 0)
end = (70, 70)

path, length = compute_path(grid, start, end)

print('Steps:', length)