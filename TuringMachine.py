op_count = (
    ['print', 1],
    ['put', 3],
    ['hashMap', 1],
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
        self.iterator = 0
        self.stack = []
        self.memory = []
        self.hashMapMemory = []
        self.op_buff = []

    def start(self):
        print('Turing machine: ')
        while self.iterator < len(self.input_stack):
            if self.isOperand(self.input_stack[self.iterator]):
                self.calculate()
            else:
                self.stack.append(self.input_stack[self.iterator])
            self.iterator = self.iterator + 1
        print(self.hashMapMemory)

        None

    def isOperand(self, operand):
        self.op_buff = None
        for oper in op_count:
            if operand == oper[0]:
                self.op_buff = oper
        if self.op_buff is not None:
            return True
        else:
            return False

    def calculate(self):
        if self.op_buff[0] == '=':
            self.memory_change(self.stack.pop(-1), self.stack.pop(-1))
        if self.op_buff[0] == '+':
            self.add(self.stack.pop(-1), self.stack.pop(-1))
        if self.op_buff[0] == '*':
            self.multiply(self.stack.pop(-1), self.stack.pop(-1))
        if self.op_buff[0] == '/':
            self.divide(self.stack.pop(-1), self.stack.pop(-1))
        if self.op_buff[0] == 'goto':
            self.goto(self.stack.pop(-1))
        if self.op_buff[0] == 'false goto':
            self.false_goto(self.stack.pop(-1))
        if self.op_buff[0] == '>':
            self.greater(self.stack.pop(-1), self.stack.pop(-1))
        if self.op_buff[0] == '<':
            self.less(self.stack.pop(-1), self.stack.pop(-1))
        if self.op_buff[0] == '-':
            self.minus(self.stack.pop(-1), self.stack.pop(-1))
        if self.op_buff[0] == '==':
            self.equals(self.stack.pop(-1), self.stack.pop(-1))
        if self.op_buff[0] == '>=':
            self.greater_equals(self.stack.pop(-1), self.stack.pop(-1))
        if self.op_buff[0] == '<=':
            self.less_equals(self.stack.pop(-1), self.stack.pop(-1))
        if self.op_buff[0] == '!=':
            self.not_equals(self.stack.pop(-1), self.stack.pop(-1))
        if self.op_buff[0] == '&':
            self.and_ex(self.stack.pop(-1), self.stack.pop(-1))
        if self.op_buff[0] == '||':
            self.or_ex(self.stack.pop(-1), self.stack.pop(-1))
        if self.op_buff[0] == 'print':
            self.print(self.stack.pop(-1))
        if self.op_buff[0] == 'hashMap':
            self.hashMap(self.stack.pop(-1))
        if self.op_buff[0] == 'put':
            self.hashMapPut(self.stack.pop(-1), self.stack.pop(-1), self.stack.pop(-1))
        None

    def hashMap(self, var):
        if self.hashMapKeyIndex(var) != -1:
            self.hashMapMemory.remove(var)
        self.hashMapMemory.append([var, {}])

    def hashMapPut(self, value, key, var):
        self.hashMapMemory[self.hashMapKeyIndex(var)][1].update({key: value})

    def hashMapGet(self, var, key):
        print(self.hashMapMemory[self.hashMapKeyIndex(var)][1].get(key))

    def hashMapKeyIndex(self, var):
        counter = 0
        for varhash in self.hashMapMemory:
            if varhash[0] == var:
                return counter
            counter = counter + 1
        return -1

    def hashMapClear(self, var):
        self.hashMapMemory[self.hashMapKeyIndex(var)][1].clear()

    def check_type(self, var):
        if self.hashMapMemory[self.hashMapKeyIndex(var)] == -1:
            return 'hashmap'
        elif self.get_var(var):
            return 'var'

    def print(self, value):
        ret_value = self.get_var(value)
        if ret_value is not None:
            print(ret_value)
        else:
            print(value)

    def goto(self, iterator):
        counter = -1
        for tokens in self.input_stack:
            counter = counter + 1
            if tokens == iterator + ':':
                self.iterator = counter

    def false_goto(self, iterator):
        counter = -1
        if self.stack.pop(-1) is False:
            for tokens in self.input_stack:
                counter = counter + 1
                if tokens == iterator + ':':
                    self.iterator = counter

    def divide(self, op2, op1):
        self.stack.append(self.convert_to_float(op1) / self.convert_to_float(op2))

    def add(self, op2, op1):
        self.stack.append(self.convert_to_float(op1) + self.convert_to_float(op2))

    def minus(self, op2, op1):
        self.stack.append(self.convert_to_float(op1) - self.convert_to_float(op2))

    def multiply(self, op2, op1):
        self.stack.append(self.convert_to_float(op1) * self.convert_to_float(op2))

    def greater(self, op2, op1):
        self.stack.append(self.convert_to_float(op1) > self.convert_to_float(op2))

    def greater_equals(self, op2, op1):
        self.stack.append(self.convert_to_float(op1) >= self.convert_to_float(op2))

    def less_equals(self, op2, op1):
        self.stack.append(self.convert_to_float(op1) <= self.convert_to_float(op2))

    def equals(self, op2, op1):
        self.stack.append(self.convert_to_float(op1) == self.convert_to_float(op2))

    def not_equals(self, op2, op1):
        self.stack.append(self.convert_to_float(op1) != self.convert_to_float(op2))

    def less(self, op2, op1):
        self.stack.append(self.convert_to_float(op1) < self.convert_to_float(op2))

    def and_ex(self, op2, op1):
        self.stack.append(op1 and op2)

    def or_ex(self, op2, op1):
        self.stack.append(op1 or op2)

    def memory_change(self, value, var):
        value = self.convert_to_float(value)
        for stored_var, stored_value in self.memory:
            if stored_var == var:
                self.memory.remove([stored_var, stored_value])
        self.memory.append([var, value])

    def get_var(self, var):
        buff = None
        for stored_var, stored_value in self.memory:
            if stored_var == var:
                buff = stored_value
        return buff

    def convert_to_float(self, op):
        if isinstance(op, str):
            for var, value in self.memory:
                if op == var:
                    op = value
                elif op == '-' + var:
                    op = -value
        return float(op)
