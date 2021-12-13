import copy
from collections import defaultdict

from days import AOCDay, day


@day(13)
class Day13(AOCDay):
    print_debug = "c12"
    test_input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5""".split("\n")

    grid = defaultdict(int)
    folds = []

    def common(self, input_data):
        points, folds = "\n".join(input_data).split("\n\n")
        points = points.split("\n")
        folds = folds.split("\n")
        self.grid = defaultdict(int)
        self.folds = []
        for line in points:
            x, y = line.split(",")
            self.grid[(int(x), int(y))] = 1
        for line in folds:
            axis, i = line.split(" ")[-1].split("=")
            self.folds.append((axis, int(i)))

    def fold(self, axis, i):
        if axis == "y":
            for x, y in [k for k in self.grid.keys()]:
                if self.grid[(x, y)] == 1 and y > i:
                    new_y = i + (i - y)
                    self.grid[(x, new_y)] = 1
                    self.grid[(x, y)] = 0
        elif axis == "x":
            for x, y in [k for k in self.grid.keys()]:
                if self.grid[(x, y)] == 1 and x > i:
                    new_x = i + (i - x)
                    self.grid[(new_x, y)] = 1
                    self.grid[(x, y)] = 0

    def part1(self, input_data):
        axis, i = self.folds[0]
        self.fold(axis, i)
        yield len([x for x in self.grid.keys() if self.grid[x] == 1])

    def part2(self, input_data):
        for axis, i in self.folds:
            self.fold(axis, i)
        keys = [k for k in self.grid.keys()]
        max_x = max(keys, key=lambda k: k[0] if self.grid[k] == 1 else 0)[0] + 1
        max_y = max(keys, key=lambda k: k[1] if self.grid[k] == 1 else 0)[1] + 1
        for y in range(0, max_y):
            line = ""
            for x in range(0, max_x):
                line += "#" if self.grid[(x, y)] == 1 else " "
            yield line
