def parse_input(data):
    files = []
    free_space = []
    for index, char in enumerate(data):
        if index % 2 == 0:
            files.append(int(char))
        else:
            free_space.append(int(char))

    blocks = []

    for i in range(len(files)):
        current_file = files[i]
        blocks.extend([i] * current_file)

        if i < len(free_space):
            current_space = free_space[i]
            if current_space > 0:
                blocks.extend(["."] * current_space)
    return blocks


def find_free_space(blocks, pointer_sx, min_space_len, pointer_dx_start):
    available_position = None
    while pointer_sx < pointer_dx_start:
        current_space_end = pointer_sx
        while blocks[current_space_end] == ".":
            current_space_end += 1

        current_space_len = current_space_end - pointer_sx

        if current_space_len >= min_space_len:
            available_position = pointer_sx
            break
        else:
            pointer_sx = current_space_end + 1
    return available_position


def move_files(blocks):
    pointer_sx = 0
    pointer_dx = len(blocks) - 1

    while pointer_sx != pointer_dx:
        if blocks[pointer_sx] != ".":
            pointer_sx += 1
        else:
            while blocks[pointer_dx] == ".":
                pointer_dx -= 1
            pointer_dx_start = pointer_dx
            while (
                blocks[pointer_dx_start - 1] != "."
                and blocks[pointer_dx_start - 1] == blocks[pointer_dx]
            ):
                pointer_dx_start -= 1
            pointer_dx_len = pointer_dx - pointer_dx_start + 1
            available_position = find_free_space(
                blocks, pointer_sx, pointer_dx_len, pointer_dx_start
            )
            if available_position:
                blocks[available_position : available_position + pointer_dx_len] = (
                    blocks[pointer_dx_start : pointer_dx + 1]
                )
                blocks[pointer_dx_start : pointer_dx + 1] = ["."] * pointer_dx_len

                pointer_dx = pointer_dx_start - 1
            else:
                pointer_dx = pointer_dx_start - 1
            pointer_sx = 0

    return blocks


def compute_checksum(blocks):
    checksum = 0
    for i in range(len(blocks)):
        if blocks[i] == ".":
            checksum += 0
        else:
            checksum += i * blocks[i]
    return checksum


data = None
with open("input.txt") as f:
    data = f.read().strip()

if data:
    blocks = parse_input(data)
    blocks = move_files(blocks)
    checksum = compute_checksum(blocks)
    print(checksum)
