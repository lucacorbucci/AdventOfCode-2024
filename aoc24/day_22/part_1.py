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
with open('input.txt', 'r') as file:
    for line in file:
        value = int(line.strip())
        for _ in range(0, final_round):
            value = next_secret_number(value)
        results.append(value)

print(sum(results))
