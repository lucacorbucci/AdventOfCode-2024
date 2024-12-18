from collections import Counter
from collections import defaultdict


def process_item(item):
    if item == 0:
        return (1,)
    elif len((item_ := str(item))) % 2 == 0:
        mid = len(item_) // 2
        return (int(item_[:mid]), int(item_[mid:]))
    else:
        return (item * 2024,)

def blink(line):
    counter = Counter(line)

    # The idea is that we do not need to keep track of all 
    # the items that we have in the list and to generate all 
    # of them. It is enough to count the occorrences of the different
    # values that we have in the list (the stones).
    # For each value in the counter what we do is to 
    # generate the next stone (they could be two or one) and then 
    # we assign as a counter for the new stones the counter of the old stones
    # Example. We have {"0", 3, "1", 4} in the  list of the stones.
    # We call the blink method, for the "0" we obtain "1" and so in the new 
    # stones dictionary we will have {"1": 3}. Then we consider "1" and we multiply it 
    # by 2048. So in the dictionary we will have {"1": 3, "2024": 4}.
    # This then continues, for instance we will have {"2048": 3, "20": 4, "24": 4}
    for i in range(75):
        next_line = defaultdict(int)
        print(counter)
        for item, occurrences in counter.items():
            for new_item in process_item(item):
                next_line[new_item] += occurrences
        counter = next_line 
    return counter

with open('input.txt') as f:
    line = map(int, f.read().strip().split())
    result = blink(line)

print(sum(result.values()))
        