import timeit

import numpy as np

from Task import Task


class Day9(Task):
    map_move = {
        "U": np.array([1, 0]),
        "D": np.array([-1, 0]),
        "L": np.array([0, -1]),
        "R": np.array([0, 1])
    }

    def part1(self):
        return self.get_number(2)

    def part2(self):
        return self.get_number(10)

    def get_number(self, n):
        rope = np.ones((n, 2))
        visited = {str(rope[-1]): True}
        for moves in self.task_input:
            move, num = self.get_round_specs(moves)
            for _ in range(num):
                rope = self.get_new_coords(rope, move)
                visited[str(rope[-1])] = True
        return len(visited.keys())

    def get_new_coords(self, rope, move):
        new_rope = rope.copy()
        for i in range(len(rope)):
            diff = move if i == 0 else new_rope[i - 1] - new_rope[i]
            next_move = self.get_move(diff, True if i == 0 else False)
            new_rope[i] += next_move
        return new_rope

    def get_round_specs(self, moves):
        move, num = moves.split()
        return self.map_move[move], int(num)

    @staticmethod
    def get_move(diff, force_move=False):
        if any(abs(diff) > 1) or force_move:
            transformed_diff = np.array(list(map(lambda x: 1 if x == 0 else x, diff)))
            m = diff / abs(transformed_diff)
            return m
        else:
            return np.array([0, 0])

    def print_solution(self):
        print("Answer to part1:", self.part1(), f"time: {round(timeit.timeit(lambda: self.part1(), number=1), 4)}s")
        print("Answer to part1:", self.part2(), f"time: {round(timeit.timeit(lambda: self.part2(), number=1), 4)}s")


if __name__ == '__main__':
    input_file_name = "../data/input9.txt"
    day = Day9(input_file_name)
    day.print_solution()
