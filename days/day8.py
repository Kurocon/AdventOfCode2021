from collections import defaultdict

from days import AOCDay, day


@day(8)
class Day8(AOCDay):
    print_debug = "c12"
    test_input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce""".split("\n")

    def common(self, input_data):
        self.input_data = [(line.split(" | ")[0].split(" "), line.split(" | ")[1].split(" ")) for line in input_data]

    def part1(self, input_data):
        yield sum(1 for line in self.input_data for digit in line[1] if len(digit) in [2, 3, 4, 7])

    def part2(self, input_data):
        out_sum = 0
        for line in self.input_data:
            # Identify numbers
            segment_counts = defaultdict(list)
            for digit in line[0]:
                segment_counts[len(digit)].append(sorted(list(digit)))
            # 1, 7, 4 and 8 are recognisable by their segment counts
            digits = {
                1: segment_counts[2][0],
                7: segment_counts[3][0],
                4: segment_counts[4][0],
                8: segment_counts[7][0]
            }
            leftover_5 = segment_counts[5]
            leftover_6 = segment_counts[6]
            # 9 is the one with 6 segments that has all edges that 4 also has
            digits[9] = [x for x in leftover_6 if all(s in x for s in digits[4])][0]
            leftover_6.remove(digits[9])
            # 0 is the one with 6 segments that has all edges that 1 also has
            digits[0] = [x for x in leftover_6 if all(s in x for s in digits[1])][0]
            leftover_6.remove(digits[0])
            # 6 is the singular leftover with 6 segments
            digits[6] = leftover_6[0]
            leftover_6.remove(digits[6])
            # 3 is the one with 5 segments that has all edges that 1 also has
            digits[3] = [x for x in leftover_5 if all(s in x for s in digits[1])][0]
            leftover_5.remove(digits[3])
            # 5 is the one with 5 segments that has all edges that both 6 and 9 have
            digits[5] = [x for x in leftover_5 if all(s in x for s in digits[6] if s in digits[9])][0]
            leftover_5.remove(digits[5])
            # 2 is the singular leftover with 5 segments
            digits[2] = leftover_5[0]
            leftover_5.remove(digits[2])

            # Identify the outputs
            output = ""
            for digit in line[1]:
                output += [str(num) for num, segments in digits.items() if sorted(list(digit)) == segments][0]
            out_sum += int(output)
        yield out_sum

