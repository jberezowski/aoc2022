from collections import deque

import numpy as np

from Task import Task

SPACE_BETWEEN_CHARACTERS = 4
TOWERS_NUM = 9


class Day5(Task):

    def __init__(self, task_input_path):
        self.task_input = self.load_input(task_input_path)
        self.state = []
        self.instructions = self.task_input[10:]

    def print_solution(self):
        print("Answer to part1:", self.part1())
        print("Answer to part2:", self.part2())

    def part1(self):
        self.state = self.load_cargo_state(self.task_input)
        for inst_raw in self.instructions:
            inst = self.parse_instruction(inst_raw)
            amount, i_from, i_to = inst[0], inst[1] - 1, inst[2] - 1  # shift indices by -1
            stack_from = self.state[i_from]
            stack_to = self.state[i_to]
            for _ in range(amount):
                stack_to.append(stack_from.pop())
        return "".join([_.pop() for _ in self.state])

    def part2(self):
        self.state = self.load_cargo_state(self.task_input)
        for inst_raw in self.instructions:
            inst = self.parse_instruction(inst_raw)
            amount, i_from, i_to = inst[0], inst[1] - 1, inst[2] - 1  # shift indices by -1
            stack_from = self.state[i_from]
            stack_to = self.state[i_to]
            temp_stack = deque()
            for _ in range(amount):
                temp_stack.append(stack_from.pop())
            for _ in range(amount):
                stack_to.append(temp_stack.pop())
        return "".join([_.pop() for _ in self.state])

    @staticmethod
    def load_cargo_state(lines):
        s = [deque() for _ in range(TOWERS_NUM)]
        for line_i in range(7, -1, -1):
            l = list(lines[line_i])
            for i, char in enumerate(l[1::SPACE_BETWEEN_CHARACTERS]):
                if not (char == " "):
                    stack = s[i]
                    stack.append(char)
        return s

    @staticmethod
    def parse_instruction(line):
        return [int(_) for _ in np.array(line.split())[[1, 3, 5]]]


if __name__ == '__main__':
    input_file_name = "../data/input5.txt"
    day = Day5(input_file_name)
    day.print_solution()
