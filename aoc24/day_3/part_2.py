import re


def scan_memory(memory):
    do_indexes = []
    dont_indexes = []
    mul_indexes = []
    mul = []
    for match in re.finditer(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", memory):
        mul_indexes.append(match.start())
        mul.append(match.groups())
    for match in re.finditer(r"do\(\)", memory):
        do_indexes.append(match.end())
    for match in re.finditer(r"don't\(\)", memory):
        dont_indexes.append(match.end())
    return do_indexes, dont_indexes, mul_indexes, mul


def compute_output(memory, hash_do, hash_dont, hash_indexes):
    do = True
    result = 0
    for index in range(len(memory)):
        if index in hash_do:
            do = True
        if index in hash_dont:
            do = False
        if index in hash_indexes and do:
            result += int(hash_indexes[index][0]) * int(hash_indexes[index][1])
    return result


with open("input.txt") as f:
    memory = f.readlines()[0]

do_indexes, dont_indexes, mul_indexes, mul = scan_memory(memory)
hash_indexes = {k: v for k, v in zip(mul_indexes, mul)}
hash_do = set(do_indexes)
hash_dont = set(dont_indexes)

print(compute_output(memory, hash_do, hash_dont, hash_indexes))
