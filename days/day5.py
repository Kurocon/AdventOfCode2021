from collections import defaultdict

from days import AOCDay, day


@day(5)
class Day5(AOCDay):
    print_debug = "c12"
    test_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".split("\n")
    lines = []
    grid = defaultdict(int)

    def common(self, input_data):
        self.lines = []
        self.grid = defaultdict(int)
        for line in input_data:
            line = line.split(" -> ")
            start = list(map(int, line[0].split(",")))
            end = list(map(int, line[1].split(",")))
            self.lines.append((start, end))

    def print_grid(self, size=10):
        for y in range(size):
            for x in range(size):
                print(self.grid[(x, y)] if self.grid[(x, y)] != 0 else ".", end="")
            print("")

    def part1(self, input_data):
        # Only consider vertical/horizontal lines
        self.lines = list(filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], self.lines))
        for start, end in self.lines:
            # Vertical lines
            if start[0] == end[0]:
                order = sorted([start[1], end[1]])
                for i in range(order[0], order[1] + 1):
                    self.grid[(start[0], i)] += 1
            # Horizontal lines
            elif start[1] == end[1]:
                order = sorted([start[0], end[0]])
                for i in range(order[0], order[1] + 1):
                    self.grid[(i, start[1])] += 1
        yield len([x for x in self.grid.values() if x > 1])

    def part2(self, input_data):
        for start, end in self.lines:
            # Vertical lines
            if start[0] == end[0]:
                order = sorted([start[1], end[1]])
                for i in range(order[0], order[1] + 1):
                    self.grid[(start[0], i)] += 1
            # Horizontal lines
            elif start[1] == end[1]:
                order = sorted([start[0], end[0]])
                for i in range(order[0], order[1] + 1):
                    self.grid[(i, start[1])] += 1
            # Diagonal lines
            else:
                x = start[0]
                y = start[1]
                self.grid[(x, y)] += 1
                while x != end[0] and y != end[1]:
                    if start[0] < end[0]:
                        x += 1
                    else:
                        x -= 1
                    if start[1] < end[1]:
                        y += 1
                    else:
                        y -= 1
                    self.grid[(x, y)] += 1
        yield len([x for x in self.grid.values() if x > 1])
