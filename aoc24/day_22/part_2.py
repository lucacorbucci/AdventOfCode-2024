from functools import lru_cache 

PRUNE = 16777216

@lru_cache(maxsize=None)
def next_secret_number(secret_number):
    # multiplying the secret number by 64
    next_value = secret_number*64
    # mix this result into the secret number
    secret_number = next_value ^ secret_number
    # prune the secret number 
    secret_number = secret_number % PRUNE

    # divide the secret number by 32
    next_value = secret_number // 32
    # mix 
    secret_number = next_value ^ secret_number
    # prune
    secret_number = secret_number % PRUNE
    
    # multiplying the secret number by 2048
    next_value = secret_number*2048
    # mix
    secret_number = next_value ^ secret_number
    # prune
    secret_number = secret_number % PRUNE
    
    return secret_number

final_round = 2000
results = []
price = []
all_sequences = set()
differences = []
sequences = []
with open('input.txt', 'r') as file:
    for line in file:
        value = int(line.strip())
        results.append(value)
        current_price = []
        current_price.append(int(str(value)[-1]))
        current_differences = []
        current_sequences = {}
        for _ in range(0, final_round):
            value = next_secret_number(value)
            results.append(value)
            current_price.append(int(str(value)[-1]))
            current_differences.append(current_price[-1] - current_price[-2])
        queue = []
        index = 0
        for diff in current_differences:
            if results[index-1] != results[index]:
                queue.append(diff)
            else:
                queue = [diff]
            if len(queue) == 4:
                if not tuple(queue) in current_sequences:
                    current_sequences[tuple(queue)] = current_price[index+1]
                all_sequences.add(tuple(queue))
                queue.pop(0)
            index += 1
        differences.append(current_differences)
        price.append(current_price)
        sequences.append(current_sequences)


max_sum = 0

for possible_sequence in all_sequences:
    tmp_sum = 0
    for sequence in sequences:
        if possible_sequence in sequence:
            tmp_sum += sequence[possible_sequence]
    if tmp_sum > max_sum:
        max_sum = tmp_sum
print(max_sum)