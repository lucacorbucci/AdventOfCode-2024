import os 
import time
import copy 

class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix
        self.original_matrix = matrix
        self.original_position = self.search_position()
        self.current_position = self.search_position()
        self.current_direction = "^"
        self.grid_size = (len(matrix), len(matrix[0]))
        self.visited_positions = set([self.current_position])
        self.path = [self.current_position]
        
    def search_position(self):
        for x, line in enumerate(self.matrix):
            for y, char in enumerate(line):
                if char == '^':
                    return (x, y) 

    def move(self):
        if self.current_direction == "^":
            return (self.current_position[0] - 1, self.current_position[1])
        elif self.current_direction == ">":
            return (self.current_position[0], self.current_position[1] + 1)
        elif self.current_direction == "v":
            return (self.current_position[0] + 1, self.current_position[1])
        elif self.current_direction == "<":
            return (self.current_position[0], self.current_position[1] - 1)
        else:
            raise ValueError("Invalid direction")

    def rotate_direction(self):
        if self.current_direction == "^":
            self.current_direction = ">"
        elif self.current_direction == ">":
            self.current_direction = "v"
        elif self.current_direction == "v":
            self.current_direction = "<"
        elif self.current_direction == "<":
            self.current_direction = "^"
        else:
            raise ValueError("Invalid direction")

    def move_guard(self, print_path=False, search_loop = False):
        loop = False
        visited_obstacle = False
        num_passes = 0
        while True:
            next_position = self.move()
            if next_position[0] < 0 or next_position[0] >= self.grid_size[0] or next_position[1] < 0 or next_position[1] >= self.grid_size[1]:
                break

            if visited_obstacle:
                num_passes += 1
                # print(num_passes, self.grid_size[0] * self.grid_size[1])
                if num_passes >= self.grid_size[0] * self.grid_size[1]:
                    loop = True
                    break

            if self.matrix[next_position[0]][next_position[1]] == "#":
                self.rotate_direction()
            elif self.matrix[next_position[0]][next_position[1]] == "O":
                num_passes += 1
                self.rotate_direction()
                visited_obstacle = True
            else:
                self.current_position = next_position
                self.matrix[next_position[0]][next_position[1]] = self.current_direction
                if print_path:
                    self.print_matrix()
                    time.sleep(0.05)
                if not search_loop:
                    self.visited_positions.add(next_position)
                    self.path.append(next_position)

        return self.count_visited(), self.path, self.visited_positions, loop

    def print_matrix(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
        for row in self.matrix:
            print("".join(row))

    def count_visited(self):
        return len(self.visited_positions)



def read_lines():
    lines = []
    with open('input.txt') as f:
        for line in f:
            lines.append(list(line.strip()))
    return lines 

matrix = Matrix(read_lines())
_, path, visited_positions, _ = matrix.move_guard()


import concurrent.futures



count_loops = 0
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     results = list(executor.map(check_loop, visited_positions))

# visited_positions = [(55,107)]

for position in visited_positions:
    if position != matrix.original_position:
        print("Evaluate position: ", position)
        new_grid = Matrix(read_lines())
        new_grid.matrix[position[0]][position[1]] = "O"
        _, _, _, loop = new_grid.move_guard(search_loop=True)
        if loop:
            count_loops += 1


print(count_loops)

print(count_loops)