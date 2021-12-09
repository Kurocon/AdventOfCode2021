from days import AOCDay, day

from collections import Counter
from functools import reduce
import numpy as np
from scipy.ndimage import label

@day(9)
class Day9(AOCDay):
    print_debug = "c12"
    test_input = """2199943210
3987894921
9856789892
8767896789
9899965678""".split("\n")

    groups = None

    def common(self, input_data):
        self.input_data = {(x, y): int(v) for y, line in enumerate(input_data) for x, v in enumerate(line)}
        self.groups = [[1 if int(v) < 9 else 0 for v in line] for line in input_data]

    def neighbours(self, x, y):
        offsets = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        return [(x + off_x, y + off_y) for off_x, off_y in offsets if (x + off_x, y + off_y) in self.input_data.keys()]

    def part1(self, input_data):
        yield sum(1 + value for coord, value in self.input_data.items() if all(self.input_data[n] > value for n in self.neighbours(*coord)))

    def part2(self, input_data):
        np_arr = np.array(self.groups)
        labeled, ncomponents = label(np_arr)
        counts = Counter([x for row in labeled for x in row if x != 0])
        top_3 = [x[1] for x in counts.most_common(3)]
        yield reduce(lambda x, y: x * y, top_3)
