wires = {}
operations = []
solved_operations = []
missing_wires = {}
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        if ":" in line:
            line = line.split(":")
            wires[line[0]] = int(line[1])
        elif "->" in line:
            line = line.split(" ")
            first_wire = line[0]
            op = line[1]
            second_wire = line[2]
            result = line[-1]
            operations.append((first_wire, second_wire, op, result))

while operations:
    operation = operations.pop(0)

    first_wire, second_wire, op, result = operation

    if first_wire not in wires or second_wire not in wires:
        if first_wire not in wires:
            if first_wire not in missing_wires:
                missing_wires[first_wire] = []
            missing_wires[first_wire].append(operation)

        if second_wire not in wires:
            if second_wire not in missing_wires:
                missing_wires[second_wire] = []
            missing_wires[second_wire].append(operation)
    else:
        match op: 
            case "AND":
                wires[result] = wires[first_wire] and wires[second_wire]
            case "OR":
                wires[result] = wires[first_wire] or wires[second_wire]
            case "XOR":
                wires[result] = wires[first_wire] ^ wires[second_wire]
        if result not in solved_operations:
            solved_operations.append(result)

        added_keys = []
        for key in missing_wires:
            if key in wires:
                for missed_op in missing_wires[key]:
                    operations.insert(0, missed_op)
                added_keys.append(key)

        for key in added_keys:
            del missing_wires[key]
binary = "".join(map(str, [wires[wire] for wire in sorted(list(filter(lambda x: x[0] == "z", solved_operations)))]))[::-1]
result = int(binary, 2)

print(binary)
print(result)