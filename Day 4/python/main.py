class Color:
    NORMAL = "\033[0m"
    YELLOW = "\033[93m"

class Board:
    def __init__(self, *args):
        self.numbers = [["0" for j in range(0, 5)] for i in range(0, 5)]
        if len(args) == 1:
            for i in range(0, 5):
                self.numbers[i] = args[0][i].split()
        self.markers = [[False for j in range(0, 5)] for i in range(0, 5)]
        self.bingo = False

    def __str__(self):
        string = ""
        for i in range(0, 5):
            for j in range(0, 5):
                if self.markers[i][j]:
                    string += Color.YELLOW + self.numbers[i][j].rjust(2) + Color.NORMAL
                else:
                    string += self.numbers[i][j].rjust(2)
                string += " "
            string += "\n" if i < 4 else ""
        return string

    def is_bingo(self):
        return self.bingo

    def set_numbers(self, board):
        for i in range(0, 5):
            for j in range(0, 5):
                self.numbers[i][j] = board[i][j]

    def set_bingo(self):
        for i in range(0, 5):
            counter = 0
            for j in range(0, 5):
                if self.markers[i][j]:
                    counter += 1
                else:
                    break
            if counter == 5:
                self.bingo = True
                return

        for j in range(0, 5):
            counter = 0
            for i in range(0, 5):
                if self.markers[i][j]:
                    counter += 1
                else:
                    break
            if counter == 5:
                self.bingo = True
                return

    def set_markers(self, number):
        for i in range(0, 5):
            for j in range(0, 5):
                if self.numbers[i][j] == number:
                    self.markers[i][j] = True
        self.set_bingo()

    def get_sum_unmarked(self):
        total = 0
        for i in range(0, 5):
            for j in range(0, 5):
                if not self.markers[i][j]:
                    total += int(self.numbers[i][j])
        return total

def part_one():
    with open("../input.txt") as file:
        lines = [line.strip() for line in file if line.strip()]
    draws = lines[0].split(",")
    boards = []
    for i in range(1, len(lines), 5):
        boards.append(Board(lines[i:i+5]))
    for draw in draws:
        for board in boards:
            board.set_markers(draw)
            if board.is_bingo():
                score = board.get_sum_unmarked() * int(draw)
                print(score)
                return

def part_two():
    with open("../input.txt") as file:
        lines = [line.strip() for line in file if line.strip()]
    draws = lines[0].split(",")
    boards = []
    for i in range(1, len(lines), 5):
        boards.append(Board(lines[i:i+5]))
    bingos = [0] * len(boards)
    for draw in draws:
        for i in range (0, len(boards)):
            boards[i].set_markers(draw)
            if boards[i].is_bingo():
                bingos[i] = 1
            if sum(bingos) == len(bingos):
                score = boards[i].get_sum_unmarked() * int(draw)
                print(score)
                return

if __name__ == "__main__":
    part_one()
    part_two()
