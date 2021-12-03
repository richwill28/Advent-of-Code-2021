def part_one():
    horizontal = 0
    depth = 0
    with open("../input.txt") as file:
        for line in file:
            command = line.split()[0]
            unit = int(line.split()[1])
            if command == "forward":
                horizontal += unit
            elif command == "down":
                depth += unit
            elif command == "up":
                depth -= unit
    print(horizontal * depth)

def part_two():
    horizontal = 0
    depth = 0
    aim = 0
    with open("../input.txt") as file:
        for line in file:
            command = line.split()[0]
            unit = int(line.split()[1])
            if command == "forward":
                horizontal += unit
                depth += aim * unit
            elif command == "down":
                aim += unit
            elif command == "up":
                aim -= unit
    print(horizontal * depth)

if __name__ == "__main__":
    part_one()
    part_two()
