import os 
import time

class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix
        self.current_position = self.search_position()
        self.current_direction = "^"
        self.grid_size = (len(matrix), len(matrix[0]))
        self.visited_positions = set(self.current_position)
        
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

    def move_guard(self, visualize_path=False):
        while True:
            next_position = self.move()
            if next_position[0] < 0 or next_position[0] >= self.grid_size[0] or next_position[1] < 0 or next_position[1] >= self.grid_size[1]:
                break
            if self.matrix[next_position[0]][next_position[1]] == "#":
                self.rotate_direction()
            else:
                self.current_position = next_position
                self.matrix[next_position[0]][next_position[1]] = self.current_direction
                if visualize_path:
                    self.print_matrix()
                    time.sleep(0.01)
                self.visited_positions.add(next_position)


        return self.count_visited()

    def print_matrix(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
        for row in self.matrix:
            print("".join(row))

    def count_visited(self):
        visited = 0
        for line in self.matrix:
            for char in line:
                if char == "^" or char == ">" or char == "v" or char == "<":
                    visited += 1
        return visited

lines = []
with open('input.txt') as f:
    for line in f:
        line 
        lines.append(list(line.strip()))

matrix = Matrix(lines)
print(matrix.move_guard(visualize_path=True))
