from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder
from enum import Enum
from collections import defaultdict

class Movements(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


def is_valid_position(x, y):
    if x < 0 or x >= len(grid[0]):
        return False
    if y < 0 or y >= len(grid):
        return False
    return True


def compute_path(grid, start, end):
    """
    Compute the path from start to end in the grid

    Returns the path and the number of operations
    """
    new_grid = []
    for line in grid:
        line = [0 if char == "#" else 1 for char in line]
        new_grid.append(list(line))

    new_grid = Grid(matrix=new_grid)
    start = new_grid.node(start[1], start[0])
    end = new_grid.node(end[1], end[0])
    finder = DijkstraFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, new_grid)

    return path, len(path) - 1


start = None
end = None
grid = []
with open("input.txt") as f:
    for y, line in enumerate(f):
        current_line = list(line.strip())
        grid.append(current_line)
        for x, char in enumerate(current_line):
            if char == "S":
                start = (y, x)
            if char == "E":
                end = (y, x)

# Compute the path from start to end
path, length = compute_path(grid, start, end)

distances = {}
for i, node in enumerate(path):
    grid[node.y][node.x] = "0"
    distances[(node.y, node.x)] = i


# I consider all the positions in the grid. For each 
# position I consider if the path from S to E pass 
# either on the left and right or up and down. If it
# does, I check if the distance between the two paths
# is greater than 100. If it is I know that removing 
# the "#" in the middle will make the path shorter.
combinations = [
    [Movements.UP.value, Movements.DOWN.value],
    [Movements.LEFT.value, Movements.RIGHT.value],
]
removed = set()
cheats = defaultdict(int)

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if grid[y][x] == "#":
            for movement in combinations:
                if (
                    is_valid_position(x + movement[0][1], y + movement[0][0])
                    and is_valid_position(x + movement[1][1], y + movement[1][0])
                    and (y, x) not in removed and grid[y + movement[0][0]][x + movement[0][1]] == "0"
                        and grid[y + movement[1][0]][x + movement[1][1]] == "0"
                ):  
                    if dist:= abs(distances[(y + movement[0][0], x + movement[0][1])] - distances[(y + movement[1][0], x + movement[1][1])]) > 100:
                        removed.add(
                            (y, x)
                        )
                        cheats[dist] += 1

print(len(removed))
