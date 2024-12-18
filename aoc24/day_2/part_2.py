def check_safety(levels: str, allow_errors: bool) -> bool:
    if isinstance(levels, str):
        levels = [int(number) for number in levels.split()]
    direction = 1 if levels[1] > levels[0] else -1

    for index in range(1, len(levels)):
        diff = (levels[index] - levels[index - 1]) * direction
        if diff < 1 or diff > 3:
            if allow_errors:
                # I need to check if I can remove the current element or the previous one
                # or the next one. There are 3 possibilities.
                return (
                    check_safety(levels[:index] + levels[index + 1 :], False)
                    or check_safety(levels[: index - 1] + levels[index:], False)
                    or check_safety(levels[: index - 2] + levels[index - 1 :], False)
                )
            else:
                return False

    return True


safety_counter = 0

with open("input.txt") as f:
    for line in f:
        if check_safety(line, True):
            safety_counter += 1

print(safety_counter)
