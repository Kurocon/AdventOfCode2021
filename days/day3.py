from days import AOCDay, day

from collections import Counter
import copy


@day(3)
class Day3(AOCDay):
    print_debug = "c12"
    test_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".split("\n")

    def common(self, input_data):
        pass

    def part1(self, input_data):
        bits_gamma = ""
        bits_epsilon = ""
        for i in range(len(self.input_data[0])):
            count = Counter((x[i] for x in self.input_data))
            if count["1"] > count["0"]:
                bits_gamma += "1"
                bits_epsilon += "0"
            else:
                bits_gamma += "0"
                bits_epsilon += "1"
        yield int(bits_gamma, base=2) * int(bits_epsilon, base=2)

    @staticmethod
    def most_common(data, i):
        count = Counter((x[i] for x in data))
        most_c = count.most_common(n=2)
        if most_c[0][1] == most_c[1][1]:
            return "1"
        else:
            return most_c[0][0]

    @staticmethod
    def least_common(data, i):
        count = Counter((x[i] for x in data))
        least_c = count.most_common(n=2)
        if least_c[0][1] == least_c[1][1]:
            return "0"
        else:
            return least_c[1][0]

    def part2(self, input_data):
        options_oxygen = copy.deepcopy(self.input_data)
        options_co2 = copy.deepcopy(self.input_data)
        oxygen_rating, co2_rating = None, None

        for i in range(len(self.input_data[0])):
            if len(options_oxygen) > 1:
                most_common_oxy = self.most_common(options_oxygen, i)
                options_oxygen = list(filter(lambda x: x[i] == most_common_oxy, options_oxygen))
                if len(options_oxygen) == 1:
                    oxygen_rating = options_oxygen[0]

            if len(options_co2) > 1:
                least_common_co2 = self.least_common(options_co2, i)
                options_co2 = list(filter(lambda x: x[i] == least_common_co2, options_co2))
                if len(options_co2) == 1:
                    co2_rating = options_co2[0]

        yield int(oxygen_rating, base=2) * int(co2_rating, base=2)
