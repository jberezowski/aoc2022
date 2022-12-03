from Task import Task


class Day3(Task):

    def print_solution(self):
        print("Answer to part1:", self.part1())
        print("Answer to part2:", self.part2())

    def part1(self):
        rucksacks = [list(content) for content in self.task_input]
        split_rucksacks = [(set(items[:int(len(items) / 2)]), set(items[int(len(items) / 2):])) for items in rucksacks]
        common_letters = [parts[0].intersection(parts[1]).pop() for parts in split_rucksacks]
        common_values = [ord(char) - 96 if char.islower() else ord(char) - 64 + 26 for char in common_letters]
        return sum(common_values)

    def part2(self):
        rucksacks_not_grouped = [list(content) for content in self.task_input]
        rucksacks = [(set(i1), set(i2), set(i3)) for i1, i2, i3 in
                     zip(rucksacks_not_grouped[0::3], rucksacks_not_grouped[1::3], rucksacks_not_grouped[2::3])]
        common_letters = [parts[0].intersection(parts[1]).intersection(parts[2]).pop() for parts in rucksacks]
        common_values = [ord(char) - 96 if char.islower() else ord(char) - 64 + 26 for char in common_letters]
        return sum(common_values)


if __name__ == '__main__':
    input_file_name = "../data/input3.txt"
    day = Day3(input_file_name)
    day.print_solution()
