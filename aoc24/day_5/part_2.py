def check_order(rules, updates):
    incorrect_updates = []
    result = 0
    for update in updates:
        valid = True
        for index, number in enumerate(update):
            previous = set(update[:index])
            if number in rules:
                if rules[number] & previous != set():
                    incorrect_updates.append(update)
                    valid = False
                    break
        if valid:
            mid = len(update) // 2
            result += update[mid]

    return incorrect_updates, result


def sort_incorrect_updates(incorrect_updates, rules):
    for update in incorrect_updates:
        index = 1
        prev_index = 0
        while True:
            if update[index] in rules:
                current_rule = rules[update[index]]
                if update[prev_index] in current_rule:
                    update[prev_index], update[index] = (
                        update[index],
                        update[prev_index],
                    )
                    index = prev_index
                    prev_index = 0
                    if index == prev_index:
                        index += 1
                else:
                    prev_index += 1
                    if prev_index == index:
                        index += 1
                if index >= len(update):
                    break
            else:
                index += 1
                if index >= len(update):
                    break

    return incorrect_updates


rules = {}
updates = []
read_rules = True
with open("input.txt") as f:
    for line in f:
        if line == "\n":
            read_rules = False
            continue

        if read_rules:
            line = line.split("|")
            first_number = int(line[0].strip())
            second_number = int(line[1].strip())
            if first_number not in rules:
                rules[first_number] = set()
            rules[first_number].add(second_number)
        else:
            current_update = [int(item) for item in line.split(",")]
            updates.append(current_update)


incorrect_updates, _ = check_order(rules, updates)
sort_incorrect_updates(incorrect_updates, rules)

print(check_order(rules, incorrect_updates)[1])
