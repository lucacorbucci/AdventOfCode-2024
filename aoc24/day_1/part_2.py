from collections import Counter
import sys

sys.setrecursionlimit(3000)


def compute_distance(left_list, right_list):
    counter = Counter(right_list)
    total_counter = 0
    for number in left_list:
        occurrences = counter.get(number, 0)
        score = number * occurrences
        total_counter += score
    return total_counter


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
