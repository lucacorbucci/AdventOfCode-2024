from itertools import product

def generate_combinations(possible_values):
    return product('+*|', repeat=possible_values)


def check_equations(test_value, values):
    combinations = generate_combinations(len(values)-1)
    for combination in combinations:
        equation = []
        for i in range(len(values)):
            equation.append(values[i])
            if i < len(values)-1:
                equation.append(combination[i])

        i = 1
        total = int(equation[0])
        while i < len(equation):
        
            if equation[i] == '+':
                total += int(equation[i+1])
            elif equation[i] == '*':
                total *= int(equation[i+1])
            elif equation[i] == '|':
                total = int(str(total) + str(equation[i+1]))
            else:
                raise Exception('Invalid operator')
            i += 2
            if total > int(test_value):
                break

        if total == int(test_value):
            return int(test_value)
    return 0

total_calibration = 0

with open('input.txt') as f:
    for line in f:
        line = line.strip()
        test_values = line.split(':')[0]
        numbers = line.split(':')[1].strip().split(' ')
        total_calibration += check_equations(test_values, numbers)

print(total_calibration)