from days import AOCDay, day


@day(4)
class Day4(AOCDay):
    print_debug = "c12"
    test_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7""".split("\n")

    num_order = None
    boards = None

    def get_columns(self, board):
        return [[line[n] for line in board] for n in range(len(board[0]))]

    def get_winner(self, board, draws):
        for line in board:
            if all(n in draws for n in line):
                return line
        for column in self.get_columns(board):
            if all(n in draws for n in column):
                return column
        return None

    def has_winner(self, board, draws):
        return self.get_winner(board, draws) is not None

    def get_unmarked(self, board, draws):
        return [n for line in board for n in line if n not in draws]

    def common(self, input_data):
        self.num_order = list(map(int, input_data[0].split(",")))
        boards = "\n".join(input_data[2:]).split("\n\n")
        self.boards = [[list(map(int, line.split())) for line in board.split("\n")] for board in boards]

    def part1(self, input_data):
        cur_draws = []
        done = False
        for draw in self.num_order:
            cur_draws.append(draw)
            for board in self.boards:
                if self.has_winner(board, cur_draws):
                    done = True
                    yield sum(self.get_unmarked(board, cur_draws)) * draw
                    break
            if done:
                break

    def part2(self, input_data):
        cur_draws = []
        done = False
        boards = self.boards
        for draw in self.num_order:
            cur_draws.append(draw)
            to_remove = []
            for i, board in enumerate(boards):
                if self.has_winner(board, cur_draws):
                    if len(boards) == 1:
                        done = True
                        yield sum(self.get_unmarked(board, cur_draws)) * draw
                        break
                    else:
                        to_remove.append(i)
            if done:
                break
            if to_remove:
                to_remove_order = sorted(to_remove, reverse=True)
                for i in to_remove_order:
                    boards.pop(i)
