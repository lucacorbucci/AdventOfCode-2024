
def match_operand(operand):
    global A, B, C
    if operand < 4:
        return operand
    elif operand == 4:
        return A
    elif operand == 5:
        return B
    elif operand == 6:
        return C
    else:
        raise ValueError(f"Invalid operand: {operand}")

def exec_instruction(opcode, operand):
    global A, B, C, output, pointer_instruction, pointer_operand
    combo = match_operand(operand)
    match opcode:
        case 0:
            # adv instruction
            A = A // 2**combo
        case 1:
            # bxl instruction
            B = B ^ operand 
        case 2:
            # bst instruction
            B = combo % 8
        case 3:
            # jnz instruction
            if A != 0:
                pointer_instruction = operand
                pointer_operand = operand + 1
                return False
        case 4:
            # bxc instruction
            B = B ^ C
        case 5:
            # out instruction
            output.append(combo % 8)
        case 6:
            # bdv instruction 
            denominator = 2**combo
            B = A // denominator
        case 7:
            # cdv instruction
            denominator = 2**combo
            C = A // denominator
    return True
    

output = []
pointer_instruction = 0
pointer_operand = 1
A = 47792830
B = 0
C = 0
program = [2,4,1,5,7,5,1,6,4,3,5,5,0,3,3,0]
states = {}
i = 0
while pointer_operand < len(program):
    opcode = program[pointer_instruction]
    operand = program[pointer_operand]
    if exec_instruction(opcode, operand):
        pointer_instruction += 2
        pointer_operand += 2
        
    
print(output)
print(",".join(map(str, output)))
output_1 = ",".join(map(str, output))
