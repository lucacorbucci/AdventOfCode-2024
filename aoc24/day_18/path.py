from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder



grid = []
with open('input_path.txt') as f:
    for line in f:
        line = [0 if char=="#" else 1 for char in line.strip()]
        grid.append(list(line))


grid = Grid(matrix=grid)

start = grid.node(0, 0)
end = grid.node(6, 6)

finder = DijkstraFinder(diagonal_movement=DiagonalMovement.never)
path, runs = finder.find_path(start, end, grid)


print('operations:', runs, 'path length:', len(path))
print(grid.grid_str(path=path, start=start, end=end))
