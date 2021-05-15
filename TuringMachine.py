import CustomData.hashMap
import CustomData.doubleLinkedList

op_count = (
    ['doubleLinkedList'],
    ['get'],
    ['remove'],
    ['print'],
    ['put'],
    ['hashMap'],
    ['='],
    ['||'],
    ['&'],
    ['~'],
    ['<'],
    ['>'],
    ['=='],
    ['<='],
    ['>='],
    ['!='],
    ['+'],
    ['-'],
    ['*'],
    ['/'],
    ['goto'],
    ['false goto']
)


class Turing:
    def __init__(self, input_stack):
        self.input_stack = input_stack
        self.iterator = 0
        self.stack = []
        self.memory = {}
        self.op_buff = []

    def start(self):
        print('Turing machine: ')
        while self.iterator < len(self.input_stack):
            if self.isOperand(self.input_stack[self.iterator]):
                self.calculate()
            else:
                self.stack.append(self.input_stack[self.iterator])
            self.iterator = self.iterator + 1
        # print(self.memory)
        # print(self.hashMapIsEmpty('a'))
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
            self.add_var(self.stack.pop(-1), self.stack.pop(-1))
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
        if self.op_buff[0] == 'doubleLinkedList':
            self.doubleLinkedList(self.stack.pop(-1))
        if self.op_buff[0] == 'put':
            if self.get_type(self.stack[-3]) == 'hashMap':
                self.hashMapPut(self.stack.pop(-1), self.stack.pop(-1), self.stack.pop(-1))
            elif self.get_type(self.stack[-3]) == 'doubleLinkedList':
                self.doubleLinkedListPut(self.stack.pop(-1), self.stack.pop(-1), self.stack.pop(-1))
        if self.op_buff[0] == 'get':
            if self.get_type(self.stack[-2]) == 'hashMap':
                self.hashMapGet(self.stack.pop(-1), self.stack.pop(-1))
            elif self.get_type(self.stack[-2]) == 'doubleLinkedList':
                self.doubleLinkedListGet(self.stack.pop(-1), self.stack.pop(-1))
        if self.op_buff[0] == 'remove':
            if self.get_type(self.stack[-2]) == 'hashMap':
                self.hashMapRemove(self.stack.pop(-1), self.stack.pop(-1))
            elif self.get_type(self.stack[-2]) == 'doubleLinkedList':
                self.doubleLinkedListRemove(self.stack.pop(-1), self.stack.pop(-1))

        None

    def get_type(self, var):
        if isinstance(self.memory[var], CustomData.hashMap.HashTable) is True:
            return 'hashMap'
        elif isinstance(self.memory[var], CustomData.doubleLinkedList.DoubleLL) is True:
            return 'doubleLinkedList'

    def print(self, value):
        ret_value = self.convert_to_float(value)
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

    def add_var(self, value, var):
        value = self.convert_to_float(value)
        self.memory[var] = value

    def get_var(self, var):
        buff = None
        for stored_var, stored_value in self.memory.items():
            if stored_var == var:
                buff = stored_value
        return buff

    def convert_to_float(self, op):
        if op in self.memory:
            return self.memory.get(op)
        elif isinstance(op, str):
            for var, value in self.memory.items():
                if op == var:
                    op = value
                elif op == '-' + var:
                    op = -value
        return float(op)

    def doubleLinkedList(self, var):
        self.memory[var] = CustomData.doubleLinkedList.DoubleLL()

    def doubleLinkedListPut(self, value, key, var):
        self.memory[var].insert(key, CustomData.doubleLinkedList.DllNode(value))

    def doubleLinkedListGet(self, value, var):
        self.stack.append(self.memory[var].get(value))

    def doubleLinkedListRemove(self, value, var):
        self.memory[var].delete(value)

    def hashMap(self, var):
        self.memory[var] = CustomData.hashMap.HashTable()

    def hashMapPut(self, value, key, var):
        self.memory[var].set_val(key, value)

    def hashMapGet(self, key, var):
        self.stack.append(self.memory[var].get_val(key))

    def hashMapRemove(self, key, var):
        self.memory[var].delete_val(key)
