from collections import defaultdict

from days import AOCDay, day


@day(6)
class Day6(AOCDay):
    print_debug = "c"
    test_input = """3,4,3,1,2"""
    timers = []
    counts = defaultdict(int)

    def common(self, input_data):
        self.timers = [int(n) for n in input_data.split(",")]
        self.counts = defaultdict(int)
        for n in self.timers:
            self.counts[n] += 1

    def do_run(self, iterations):
        self.debug(f"Initial state: {self.counts}")
        for i in range(iterations):
            new_counts = defaultdict(int)
            for n, count in self.counts.items():
                n -= 1
                if n == -1:
                    n = 6
                    new_counts[n] += count
                    new_counts[8] += count
                else:
                    new_counts[n] += count
            self.counts = new_counts
            self.debug(f"After {i} days: {self.counts}")
        return sum(self.counts.values())

    def part1(self, input_data):
        yield self.do_run(80)

    def part2(self, input_data):
        yield self.do_run(256)
