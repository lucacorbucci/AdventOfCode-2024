import re


def scan_corrupted_memory(memory):
    return re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", memory)


def compute_result(matches):
    result = 0
    for match in matches:
        if (
            int(match[0]) > 0
            and int(match[1]) > 0
            and int(match[0]) < 1000
            and int(match[1]) < 1000
        ):
            result += int(match[0]) * int(match[1])
    return result


with open("input.txt") as f:
    memory = f.readlines()[0]

matches = scan_corrupted_memory(memory)
print(compute_result(matches))
