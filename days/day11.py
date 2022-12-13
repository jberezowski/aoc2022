import operator
from collections import deque

import numpy as np

from Task import Task

unwanted_chars = [":", ","]
ops = {"+": operator.add, "*": operator.mul}


class Monkey:
    def __init__(self, lines):
        for line in lines:
            filtered_init_lines = ''.join([c for c in line if c not in unwanted_chars])
            match filtered_init_lines.split():
                case ['Monkey', index]:
                    self.index = int(index)
                case ['Starting', 'items', *items]:
                    self.items = deque(list(map(int, items)))
                case ['Operation', 'new', '=', 'old', operand, val]:
                    self.operation = lambda x: ops[operand](x, x if val == "old" else int(val))
                case ['Test', 'divisible', 'by', divisor]:
                    self.divisor = int(divisor)
                case ['If', 'true', 'throw', 'to', 'monkey', index]:
                    self.monkey_index_true = int(index)
                case ['If', 'false', 'throw', 'to', 'monkey', index]:
                    self.monkey_index_false = int(index)
        self.inspection_counter = 0

    def throw_item(self, divide=True):
        item = self.items.popleft()
        self.inspection_counter += 1
        new_val = self.operation(item)
        if divide:
            new_val = new_val // 3
        monkey_index = self.monkey_index_true if new_val % self.divisor == 0 else self.monkey_index_false
        return new_val, monkey_index

    def receive_item(self, item):
        self.items.append(item)

    def __str__(self):
        return "Monkey " + str(self.index)

    def __repr__(self):
        return "Monkey " + str(self.index)


class Day11(Task):

    # def get_divisors(self):

    def print_solution(self):
        print("Answer to part1:", self.part1())
        print("Answer to part2:", self.part2())

    def part1(self):
        monkeys = self.get_monkeys(self.task_input)
        rounds = 20
        for _ in range(rounds):
            for monkey in monkeys:
                while monkey.items:
                    new_item, monkey_index = monkey.throw_item(divide=True)
                    monkeys[monkey_index].receive_item(new_item)

        n, m = sorted([m.inspection_counter for m in monkeys])[-2:]
        return m * n

    def part2(self):
        monkeys = self.get_monkeys(self.task_input)
        divisors = 1

        for monkey in monkeys:
            if divisors % monkey.divisor != 0:
                divisors *= monkey.divisor

        rounds = 10000
        for _ in range(rounds):
            for monkey in monkeys:
                while monkey.items:
                    new_item, monkey_index = monkey.throw_item(divide=False)
                    new_item = new_item % divisors
                    monkeys[monkey_index].receive_item(new_item)

        n, m = sorted([m.inspection_counter for m in monkeys])[-2:]
        return m * n

    def get_monkeys(self, lines):
        monkeys = []
        for i_line in range(0, len(lines), 7):
            new_monkey = Monkey(lines[i_line:i_line + 6])
            monkeys.append(new_monkey)
        return monkeys


if __name__ == '__main__':
    input_file_name = "../data/input11.txt"
    day = Day11(input_file_name)
    day.print_solution()
