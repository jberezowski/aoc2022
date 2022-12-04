from Task import Task


class Day4(Task):

    def print_solution(self):
        print("Answer to part1:", self.part1())
        print("Answer to part2:", self.part2())

    def part1(self):
        min_max_ranges = [[[int(_) for _ in x.split("-")] for x in line.split(",")] for line in self.task_input]
        is_overlapped = list(map(lambda items: self.mapping_part_1(items), min_max_ranges))
        return sum(is_overlapped)

    def part2(self):
        min_max_ranges = [[[int(_) for _ in x.split("-")] for x in line.split(",")] for line in self.task_input]
        is_overlapped = list(map(lambda items: self.mapping_part_2(items), min_max_ranges))
        return sum(is_overlapped)

    @staticmethod
    def mapping_part_1(items):
        return 1 if ((items[0][0] >= items[1][0] and items[0][1] <= items[1][1]) or (
                items[1][0] >= items[0][0] and items[1][1] <= items[0][1])) else 0

    @staticmethod
    def mapping_part_2(items):
        return 1 if ((items[1][0] <= items[0][0] <= items[1][1]) or (
                items[0][0] <= items[1][0] <= items[0][1])) else 0


if __name__ == '__main__':
    input_file_name = "../data/input4.txt"
    day = Day4(input_file_name)
    day.print_solution()
