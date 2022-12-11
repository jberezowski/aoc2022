from collections import deque

import numpy as np

from Task import Task


class Day10(Task):

    def print_solution(self):
        print("Answer to part1:", self.part1())
        print("Answer to part2:", self.part2())

    def part1(self):
        commands = self.get_commands(self.task_input)

        relevant_signals = np.array(list(range(20, 222, 40)))
        state_values = [1]
        scheduled = 1
        for clock in range(0, 220):
            val = state_values[-1] if len(state_values) > 0 else 1
            if scheduled <= clock:
                delta_time, delta_val = commands.pop()
                scheduled += delta_time
                val += delta_val
            state_values.append(val)
        return (np.array(state_values)[relevant_signals - 1] * relevant_signals).sum()

    def part2(self):
        screen_size = 240
        row_size = 40
        commands = self.get_commands(self.task_input)
        state_values = [1]
        scheduled = 1
        screen = ["."]
        for clock in range(0, screen_size):
            val = state_values[-1] if len(state_values) > 0 else 1
            screen.append("#" if 0 <= (clock % row_size) - val < 3 else ".")
            if scheduled <= clock:
                delta_time, delta_val = commands.pop()
                scheduled += delta_time
                val += delta_val
            state_values.append(val)

        screen = np.array(screen).reshape(screen_size / row_size, row_size)
        self.print_screen(screen)

    @staticmethod
    def print_screen(screen):
        for row in screen:
            print("".join(row))

    @staticmethod
    def get_commands(input):
        commands = deque()
        for command in input:
            match command.split():
                case ["addx", val]:
                    commands.appendleft((2, int(val)))
                case ["noop"]:
                    commands.appendleft((1, 0))
                case _:
                    raise RuntimeError(f"Unknown command")
        return commands


if __name__ == '__main__':
    input_file_name = "../data/input10.txt"
    day = Day10(input_file_name)
    day.print_solution()
