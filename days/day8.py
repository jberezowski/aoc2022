import numpy as np

from Task import Task


class Day8(Task):

    def print_solution(self):
        print("Answer to part1:", self.part1())
        print("Answer to part2:", self.part2())

    def part1(self):
        treemap = np.array([np.array(list(_), dtype=int) for _ in self.task_input])
        counter = 2 * (treemap.shape[0] + treemap.shape[1] - 2)
        for row in range(1, treemap.shape[0] - 1):
            for col in range(1, treemap.shape[1] - 1):
                if self.is_higher(row, col, treemap):
                    counter += 1
        return counter

    def part2(self):
        treemap = np.array([np.array(list(_), dtype=int) for _ in self.task_input])
        highest_score = 0
        print(treemap)
        for row in range(1, treemap.shape[0] - 1):
            for col in range(1, treemap.shape[1] - 1):
                score = self.visible_trees_multiplies(row, col, treemap)
                if score > highest_score:
                    highest_score = score
        return highest_score

    def visible_trees_multiplies(self, row, col, treemap):
        height = treemap[row, col]
        return (self.visible_trees_one_direction(height, treemap[row, 0:col][::-1]) *
                self.visible_trees_one_direction(height, treemap[row, col + 1:]) *
                self.visible_trees_one_direction(height, treemap[0:row, col][::-1]) *
                self.visible_trees_one_direction(height, treemap[row + 1:, col]))

    @staticmethod
    def visible_trees_one_direction(height, elements):
        for i in range(len(elements)):
            if height <= elements[i]:
                return i + 1
        return max(1, len(elements))

    def is_higher(self, row, col, treemap):
        height = treemap[row, col]
        return (self.is_greater_than_elements(height, treemap[row, 0:col]) or
                self.is_greater_than_elements(height, treemap[row, col + 1:]) or
                self.is_greater_than_elements(height, treemap[0:row, col]) or
                self.is_greater_than_elements(height, treemap[row + 1:, col]))

    @staticmethod
    def is_greater_than_elements(height, elements):
        return all(height > _ for _ in elements)


if __name__ == '__main__':
    input_file_name = "../data/input8.txt"
    day = Day8(input_file_name)
    day.print_solution()
