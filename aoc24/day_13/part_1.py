def solve(start, A, B):
    tmp_result = 0
    for i in range(100, 0, -1):
        if ((start[0] - i*B[0]) % A[0] == 0) and (((start[1] - i*B[1]) % A[1]) == 0):
            # print(i, (start[0] - i*B[0]) // A[0])
            assert ((start[0] - i*B[0]) // A[0])*A[0] + i*B[0] == start[0]
            assert ((start[1] - i*B[1]) // A[1])*A[1] + i*B[1] == start[1]
            if (start[0] - i*B[0]) // A[0] <= 100 and (start[1] - i*B[1]) // A[1] <= 100 and ((start[0] - i*B[0]) // A[0])  == ((start[1] - i*B[1]) // A[1]):
                # return i + 3*((start[0] - i*B[0]) // A[0])
                tmp_result = i + 3*((start[0] - i*B[0]) // A[0])

    tmp_result_2 = 0
    for i in range(0, 100):
        if ((start[0] - i*A[0]) % B[0] == 0) and (((start[1] - i*A[1]) % B[1]) == 0):
            # print(i, (start[0] - i*A[0]) // B[0])
            assert ((start[0] - i*A[0]) // B[0])*B[0] + i*A[0] == start[0]
            assert ((start[1] - i*A[1]) // B[1])*B[1] + i*A[1] == start[1]
            if (start[0] - i*A[0]) // B[0] <= 100 and (start[1] - i*A[1]) // B[1] <= 100 and ((start[0] - i*A[0]) // B[0]) == ((start[1] - i*A[1]) // B[1]):
                # return i + 3*((start[0] - i*A[0]) // B[0])
                tmp_result_2 = (start[0] - i*A[0]) // B[0] + i*3
                break
            
    print(tmp_result, tmp_result_2)

    assert tmp_result == tmp_result_2
    
    return tmp_result_2
    
machines = []
with open("input.txt") as file:
    for line in file:
        if line == "\n":
            machines.append((A, B, P))
        else:
            line = line.strip()

            if "A:" in line:
                A = (int(line.split(",")[0][-2:]), int(line.split("+")[-1]))
            if "B:" in line:
                B = (int(line.split(",")[0][-2:]), int(line.split("+")[-1]))
            if "Prize:" in line:
                P = (int(line.split(",")[0].split("=")[-1]), int(line.split("=")[-1]))
    machines.append((A, B, P))
# print(len(machines), machines)
result = 0     
for A, B, P in machines:
    tmp = solve(P, A, B)
    # print("tmp: ", tmp)
    result += tmp

print(result)