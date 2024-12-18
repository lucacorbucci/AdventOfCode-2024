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


def move_files(blocks):
    pointer_sx = 0
    pointer_dx = len(blocks) - 1

    while pointer_sx < pointer_dx:
        if blocks[pointer_sx] != ".":
            pointer_sx += 1
        else:
            if blocks[pointer_dx] == ".":
                pointer_dx -= 1
            else:
                blocks[pointer_sx], blocks[pointer_dx] = (
                    blocks[pointer_dx],
                    blocks[pointer_sx],
                )
                pointer_sx += 1
                pointer_dx -= 1
    return blocks


def compute_checksum(blocks):
    checksum = 0
    for i in range(len(blocks)):
        if blocks[i] == ".":
            break
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
