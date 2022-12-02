class Task:
    def __init__(self, task_input_path):
        self.task_input = self.load_input(task_input_path)

    @staticmethod
    def load_input(file_path):
        with open(file_path) as file:
            lines = file.readlines()
            return [line.rstrip() for line in lines]

    def solve(self):
        self.print_solution(self.task_input)