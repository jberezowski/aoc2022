import functools

import numpy

from Task import Task


class Day13(Task):

    def print_solution(self):
        print("Answer to part1:", self.part1())
        print("Answer to part2:", self.part2())

    def part1(self):
        pairs = self.get_pairs()
        indices = []
        for i in range(len(pairs)):
            (a, b) = pairs[i]
            if self.compare(a, b) == 1:
                indices.append(i + 1)
        return sum(indices)

    def part2(self):
        all_lines = [eval(line) for i, line in enumerate(self.task_input) if (i + 1) % 3 != 0]
        indices = []
        sorted_lines = sorted(all_lines, key=functools.cmp_to_key(self.compare), reverse=True)
        for i, item in enumerate(sorted_lines):
            str_item = str(sorted_lines[i])
            if str([[2]]) == str_item or str([[6]]) == str_item:
                indices.append(i + 1)
        return numpy.prod(indices)

    def compare(self, first, second):
        for a, b in zip(first, second):
            if type(a) is not list and type(b) is not list:
                if a < b:
                    return 1
                elif b < a:
                    return -1
            elif type(a) is list and type(b) is list:
                is_right = self.compare(a, b)
                if is_right != 0: return is_right
            elif type(a) is not list and type(b) is list:
                is_right = self.compare([a], b)
                if is_right != 0: return is_right
            elif type(a) is list and type(b) is not list:
                is_right = self.compare(a, [b])
                if is_right != 0: return is_right
        if len(first) < len(second):
            return 1
        elif len(second) < len(first):
            return -1
        return 0

    def get_pairs(self):
        pairs = []
        for i in range(0, len(self.task_input), 3):
            pairs.append((eval(self.task_input[i]), eval(self.task_input[i + 1])))
        return pairs


if __name__ == '__main__':
    input_file_name = "../data/input13.txt"
    day = Day13(input_file_name)
    day.print_solution()
