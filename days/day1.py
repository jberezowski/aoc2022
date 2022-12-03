import numpy as np
import pandas as pd

from Task import Task


class Day1(Task):

    def print_solution(self):
        print("Answer to part1:", self.part1())
        print("Answer to part2:", self.part2())

    def part1(self):
        elfs_calories = "" \
            .join(list(map(lambda x: x.replace("", '-'), self.task_input))) \
            .replace("---", " ").split()
        print(elfs_calories)
        elfs_calories_sum = [sum([int(numbers.replace("-", "")) for numbers in row.split("--")]) for row in
                             elfs_calories]
        return max(elfs_calories_sum)

    def part2(self):
        elfs_calories = "" \
            .join(list(map(lambda x: x.replace("", '-'), self.task_input))) \
            .replace("---", " ").split()
        print(elfs_calories)
        elfs_calories_sum = [sum([int(numbers.replace("-", "")) for numbers in row.split("--")]) for row in
                             elfs_calories]
        elfs_calories_sum = np.array(elfs_calories_sum)
        top_args = elfs_calories_sum.argsort()[-3:]
        return elfs_calories_sum[top_args].sum()

    def count_increases(self, window):
        pass
        # return np.sum(np.diff(pd.Series(self.task_input).rolling(window).sum()) > 0)


if __name__ == '__main__':
    input_file_name = "../data/input1.txt"
    day = Day1(input_file_name)
    day.print_solution()
