from days import AOCDay, day


@day(1)
class Day1(AOCDay):
    print_debug = "c12"
    test_input = """199
200
208
210
200
207
240
269
260
263""".split("\n")

    def common(self, input_data):
        self.input_data = list(map(int, self.input_data))

    def part1(self, input_data):
        increasing = 0
        for i, value in enumerate(self.input_data):
            try:
                if self.input_data[i+1] > self.input_data[i]:
                    increasing += 1
            except IndexError:
                break
        yield increasing

    def part2(self, input_data):
        increasing = 0
        prev_sum = 0
        for i, value in enumerate(self.input_data):
            try:
                new_sum = self.input_data[i] + self.input_data[i+1] + self.input_data[i+2]
                if new_sum > prev_sum:
                    increasing += 1
                prev_sum = new_sum
            except IndexError:
                break
        yield increasing - 1
