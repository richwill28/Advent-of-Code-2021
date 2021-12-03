def check_bits(line, zeros, ones):
    for i in range(0, len(line)):
        if line[i] == "0":
            zeros[i] += 1
        elif line[i] == "1":
            ones[i] += 1

def find_gamma(zeros, ones):
    gamma = ""
    for i in range(0, len(zeros)):
        if (zeros[i] > ones[i]):
            gamma += "0"
        else:
            gamma += "1"
    return gamma

def find_epsilon(zeros, ones):
    epsilon = ""
    for i in range(0, len(zeros)):
        if (zeros[i] < ones[i]):
            epsilon += "0"
        else:
            epsilon += "1"
    return epsilon

def bin_to_dec(bin):
    dec = 0
    for i in range(0, len(bin)):
        n = len(bin) - i - 1
        dec += (2 ** n) * int(bin[i])
    return dec

def part_one():
    with open("input.txt") as file:
        line = file.readline().strip()
        zeros = [0] * len(line)
        ones = [0] * len(line)
        check_bits(line, zeros, ones)
        for line in file:
            check_bits(line.strip(), zeros, ones)
    gamma = bin_to_dec(find_gamma(zeros, ones))
    epsilon = bin_to_dec(find_epsilon(zeros, ones))
    print(gamma * epsilon)

def find_oxygen(lines):
    i = 0
    while len(lines) > 1:
        zero = 0
        one = 0
        for line in lines:
            if line[i] == "0":
                zero += 1
            elif line[i] == "1":
                one += 1
        if one >= zero:
            lines = [line for line in lines if line[i] == "1"]
        else:
            lines = [line for line in lines if line[i] == "0"]
        i += 1
    return lines[0]

def find_co2(lines):
    i = 0
    while len(lines) > 1:
        zero = 0
        one = 0
        for line in lines:
            if line[i] == "0":
                zero += 1
            elif line[i] == "1":
                one += 1
        if zero <= one:
            lines = [line for line in lines if line[i] == "0"]
        else:
            lines = [line for line in lines if line[i] == "1"]
        i += 1
    return lines[0]

def part_two():
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        oxygen = bin_to_dec(find_oxygen(lines))
        co2 = bin_to_dec(find_co2(lines))
        print(oxygen * co2)

if __name__ == "__main__":
    part_one()
    part_two()
