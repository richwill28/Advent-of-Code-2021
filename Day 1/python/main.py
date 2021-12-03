def part_one():
    with open("../input.txt") as file:
        lines = file.readlines()
    counter = 0
    measurements = [int(line) for line in lines]
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i - 1]:
            counter += 1
    print(counter)

def part_two():
    with open("../input.txt") as file:
        lines = file.readlines()
    counter = 0
    measurements = [int(line) for line in lines]
    for i in range(0, len(measurements) - 3):
        first_window = measurements[i] + measurements[i + 1] + measurements[i + 2]
        second_window = measurements[i + 1] + measurements[i + 2] + measurements[i + 3]
        if second_window > first_window:
            counter += 1
    print(counter)

if __name__ == "__main__":
    part_one()
    part_two()
