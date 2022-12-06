from Task import Task


class Day6(Task):

    def print_solution(self):
        print("Answer to part1:", self.part1())
        print("Answer to part2:", self.part2())

    def part1(self):
        code = list(self.task_input[0])
        return self.search_list_for_unique_window(code, window_size=4)

    def part2(self):
        code = list(self.task_input[0])
        return self.search_list_for_unique_window(code, window_size=14)

    @staticmethod
    def search_list_for_unique_window(l, window_size):
        for i in range(window_size, len(l)):
            window = list(set(l[i - window_size: i]))
            if len(window) == window_size:
                return i


if __name__ == '__main__':
    input_file_name = "../data/input6.txt"
    day = Day6(input_file_name)
    day.print_solution()
