import sys

sys.setrecursionlimit(3000)


def compute_distance(left_list, right_list):
    if len(left_list) == 0:
        return 0

    distance = abs(left_list.pop(0) - right_list.pop(0))

    return distance + compute_distance(left_list, right_list)


left_list = []
right_list = []

with open("input.txt") as f:
    for line in f:
        left_num = line.split("   ")[0]
        right_num = line.split("   ")[1]
        left_list.append(int(left_num))
        right_list.append(int(right_num))

left_list.sort()
right_list.sort()
print(compute_distance(left_list, right_list))
