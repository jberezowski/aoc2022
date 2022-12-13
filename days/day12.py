# from collections import deque
from collections import deque

import numpy as np

from Task import Task


class Day12(Task):

    def print_solution(self):
        print("Answer to part1:", self.part1())
        print("Answer to part2:", self.part2())

    def part1(self):
        hmap = np.array([[ord(x) for x in list(row)] for row in self.task_input])
        start = [_[0] for _ in np.where(hmap == ord("S"))]
        end = [_[0] for _ in np.where(hmap == ord("E"))]
        return self.bfs(start, end, hmap)

    def part2(self):
        hmap = np.array([[ord(x) for x in list(row)] for row in self.task_input])
        end = [_[0] for _ in np.where(hmap == ord("E"))]
        distances_to_end = []
        for i in range(hmap.shape[0]):
            for j in range(hmap.shape[1]):
                if ord("a") == hmap[i, j]:
                    distances_to_end.append(self.bfs([i, j], end, hmap))
        return min(distances_to_end)

    def bfs(self, start, end, hmap):  # bidirectional BFS
        hmap[tuple(start)] = ord("a")
        hmap[tuple(end)] = ord("z")
        visited_start = {str(start): 0}
        visited_end = {str(end): 0}
        bfs_queue = deque([(start, 0, False), (end, 0, True)])
        while bfs_queue:
            pos, moves_num, reverse = bfs_queue.popleft()
            if (not reverse and str(pos) in visited_end) or (reverse and str(pos) in visited_start):
                return moves_num + (visited_start[str(pos)] if reverse else visited_end[str(pos)])
            for possible_move in self.get_possible_move(pos, hmap, visited_start, visited_end, reverse):
                if reverse:
                    visited_end[str(possible_move)] = moves_num + 1
                else:
                    visited_start[str(possible_move)] = moves_num + 1
                bfs_queue.append((possible_move, moves_num + 1, reverse))
        return np.inf

    @staticmethod
    def get_possible_move(pos, hmap, visited_start, visited_end, reverse):
        possible_moves = []
        for delta_pos in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            current_val = hmap[tuple(pos)]
            next_pos = [i + d for i, d in zip(pos, delta_pos)]
            if (0 <= next_pos[0] < hmap.shape[0]) and (0 <= next_pos[1] < hmap.shape[1]):
                next_val = hmap[tuple(next_pos)]
                is_diff_ok = (next_val - current_val <= 1) if not reverse else (-1 <= next_val - current_val <= 0)
                is_not_cached = (str(next_pos) not in visited_end) if reverse else (str(next_pos) not in visited_start)
                if is_not_cached and is_diff_ok:
                    possible_moves.append(next_pos)
        return possible_moves


if __name__ == '__main__':
    input_file_name = "../data/input12.txt"
    day = Day12(input_file_name)
    day.print_solution()
