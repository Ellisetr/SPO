op_count = (
    ['=', 2],
    ['||', 2],
    ['&', 2],
    ['~', 2],
    ['<', 2],
    ['>', 2],
    ['==', 2],
    ['<=', 2],
    ['>=', 2],
    ['!=', 2],
    ['+', 2],
    ['-', 2],
    ['*', 2],
    ['/', 2],
    ['goto', 1],
    ['false goto', 1]
)


class Turing:
    def __init__(self, input_stack):
        self.input_stack = input_stack
        self.iterator = iter(self.input_stack)
        self.stack = []
        self.memory = [[], []]

    def start(self):
        print('Turing machine: ')
        print(next(self.iterator))
        while len(self.input_stack) > 0:
            None
        None

    def calculate(self, op1, op2):
        None

    def assign(self, op1, op2):
        None






    def divide(self, op1, op2):
        return op1 / op2

    def add(self, op1, op2):
        return op1 + op2

    def multiply(self, op1, op2):
        return op1 * op2

    def greater(self, op1, op2):
        return op1 > op2

    def mapVar(self, var, value):
        if self.memory.__contains__(var):
            self.memory.remove(var)
        self.memory.append([var, value])
