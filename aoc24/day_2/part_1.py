def check_safety(line: str) -> bool:
    levels = [int(number) for number in line.split()]
    levels_shifted = levels[1:]
    increasing = None
    for original, shifted in zip(levels, levels_shifted):
        if increasing is None:
            increasing = original <= shifted
        if abs(original - shifted) > 3 or abs(original - shifted) < 1:
            return False
        if original <= shifted and not increasing:
            return False
        if original >= shifted and increasing:
            return False

    return True


safety_counter = 0

with open("input.txt") as f:
    for line in f:
        if check_safety(line):
            safety_counter += 1

print(safety_counter)
