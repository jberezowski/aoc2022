import numpy as np
import pandas as pd

from Task import Task


class Day2(Task):
    score_map_initial = {"A": {"X": 1 + 3, "Y": 2 + 6, "Z": 3 + 0}, "B": {"X": 1 + 0, "Y": 2 + 3, "Z": 3 + 6},
                         "C": {"X": 1 + 6, "Y": 2 + 0, "Z": 3 + 3}}

    score_map_correct = {"A": {"X": 3 + 0, "Y": 1 + 3, "Z": 2 + 6}, "B": {"X": 1 + 0, "Y": 2 + 3, "Z": 3 + 6},
                         "C": {"X": 2 + 0, "Y": 3 + 3, "Z": 1 + 6}}

    def print_solution(self):
        print("Answer to part1:", self.part1())
        print("Answer to part2:", self.part2())

    def part1(self):
        return self.score(self.score_map_initial)

    def part2(self):
        return self.score(self.score_map_correct)

    def score(self, score_map):
        games = [game.split() for game in self.task_input]
        scores = [score_map[round[0]][round[1]] for round in games]
        return np.array(scores).sum()


if __name__ == '__main__':
    input_file_name = "../data/input2.txt"
    day = Day2(input_file_name)
    day.print_solution()
