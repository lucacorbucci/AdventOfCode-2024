def check_order(rules, updates):
    result = 0
    for update in updates:
        valid = True
        for index, number in enumerate(update):
            previous = set(update[:index])
            if number in rules:
                if rules[number] & previous != set():
                    valid = False
                    break
        if valid:
            mid = len(update) // 2
            result += update[mid]
    return result


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


print(check_order(rules, updates))
