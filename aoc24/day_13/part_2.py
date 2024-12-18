def cramer(start, A, B):
    D = (A[0] * B[1]) - (A[1] * B[0])
    if D == 0:
        return 0 
    Dx = start[0] * B[1]  - start[1] * B[0]
    Dy = A[0] * start[1] - A[1] * start[0]
    # print(D, Dx, Dy)
    x = Dx / D if Dx % D == 0 else 0
    y = Dy / D if Dy % D == 0 else 0
    if (start[0] - (x*A[0] + y*B[0])) == 0 and (start[1] - (x*A[1] + y*B[1])) == 0:
        return int(x * 3 + y * 1)
    else:
        return 0
    
machines = []
with open("input.txt") as file:
    for line in file:
        if line == "\n":
            machines.append((A, B, P, P_))
        else:
            line = line.strip()

            if "A:" in line:
                A = (int(line.split(",")[0][-2:]), int(line.split("+")[-1]))
            if "B:" in line:
                B = (int(line.split(",")[0][-2:]), int(line.split("+")[-1]))
            if "Prize:" in line:
                P = (int(line.split(",")[0].split("=")[-1]), int(line.split("=")[-1]))
                P_ = (10000000000000+int(line.split(",")[0].split("=")[-1]), 10000000000000+int(line.split("=")[-1]))

    machines.append((A, B, P, P_))

result = 0     
for A, B, P, P_ in machines:
    result += cramer(P_, A, B)

    

print(result)
