from Task import Task


class Dir:

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.dirs = []
        self.files = []

    def to_string(self):
        path_items = []
        current_node = self
        while current_node:
            path_items.append(current_node.name)
            current_node = current_node.parent
        return "-".join(path_items)

    def size(self, count_deep=True):
        curr_sum = sum([f.size for f in self.files])
        if count_deep:
            for d in self.dirs:
                curr_sum += d.size(count_deep=True)
        return curr_sum


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Day7(Task):

    def print_solution(self):
        print("Answer to part1:", self.part1())
        print("Answer to part2:", self.part2())

    def part1(self):
        nodes = self.parse_lines(self.task_input)
        sizes = [nodes[_].size(count_deep=True) for _ in nodes.keys()]
        return sum(_ for _ in sizes if _ <= 100000)

    def part2(self):
        nodes = self.parse_lines(self.task_input)
        complete_size = nodes["/"].size()
        sizes = [nodes[_].size() for _ in nodes.keys() if complete_size - nodes[_].size() <= 70000000 - 30000000]
        return min(_ for _ in sizes)

    def parse_lines(self, lines):
        node_map = {"/": Dir("/", parent=None)}
        current_node = None
        for line in lines:
            elements = line.split()
            if "$" in elements:
                if "cd" == elements[1] and elements[2] == "..":
                    current_node = current_node.parent
                elif "cd" == elements[1] and elements[2] not in ("..", "ls"):
                    name = elements[2]
                    current_node = Dir(name, parent=current_node)
                    if current_node.parent:
                        current_node.parent.dirs.append(current_node)
                    node_map[current_node.to_string()] = current_node
            else:
                if "dir" != elements[0]:
                    current_node.files.append(File(elements[1], size=int(elements[0])))
        return node_map


if __name__ == '__main__':
    input_file_name = "../data/input7.txt"
    day = Day7(input_file_name)
    day.print_solution()
