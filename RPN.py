import copy
import re

import Parser

op = (
    ['if', 0, '', ''],
    ['while', 0, '', ''],
    ['(', 0],
    ['{', 0],
    [')', 1],
    ['{', 1],
    ['else', 1],
    ['then', 1],
    ['do', 1],
    ['=', 2],
    ['||', 2],
    ['&', 3],
    ['~', 4],
    ['<', 5],
    ['>', 5],
    ['==', 5],
    ['<=', 5],
    ['>=', 5],
    ['!=', 5],
    ['+', 6],
    ['-', 6],
    ['*', 7],
    ['/', 7]
)


class Node:
    def __init__(self, param):
        self.param = param
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)

    def printNode(self):
        for nodes in self.nodes:
            print(nodes)

    def getNodes(self):
        return self.nodes

    def getParam(self):
        return self.param


class RPN:
    def __init__(self, tree, tokens):
        self.stack = []
        self.out = []
        self.tokens = tokens
        self.mi = 1
        self.tree = Node('')
        self.tree = copy.deepcopy(tree)
        # Parser.AST(tree, 0)

    # Начало создания RPN
    def start(self):
        newtree = self.tree.getNodes()
        for node in newtree:
            for child in node.getNodes():
                self.expr(child)
        print('STACK', self.stack, ' OUT:', self.out)

    # RPN для expr
    def expr(self, node):
        if node.getParam() == 'assign_expr':
            self.assign_expr(generateTokenList(node, []))
        elif node.getParam() == 'if_expr':
            self.if_expr(node)
        elif node.getParam() == 'while_expr':
            self.while_expr(node)
        elif node.getParam() == 'do_while_expr':
            self.do_while_expr(node)

    # RPN для логических и арифметических операций
    def assign_expr(self, token_buff):
        while len(token_buff) > 0:
            print('STACK', self.stack, ' OUT:', self.out)

            if token_buff[0][0] == 'VAR' or token_buff[0][0] == 'NUMBER':
                self.out.append(token_buff.pop(0)[1])

            elif token_buff[0][0] == 'ASSIGN_OP' or token_buff[0][0] == 'OP' or token_buff[0][0] == 'LOGICAL_OP':
                for oper in op:
                    if token_buff[0][1] == oper[0]:
                        op_buff = oper

                while (len(self.stack) > 0) and (self.stack[-1][1] > op_buff[1]) and self.stack[-1][0] != '(':
                    self.out.append(self.stack.pop(-1)[0])

                token_buff.pop(0)
                self.stack.append(op_buff)

            elif token_buff[0][1] == '(':
                for oper in op:
                    if token_buff[0][1] == oper[0]:
                        op_buff = oper

                token_buff.pop(0)
                self.stack.append(op_buff)

            elif token_buff[0][1] == ')':
                for oper in op:
                    if token_buff[0][1] == oper[0]:
                        op_buff = oper
                token_buff.pop(0)

                while self.stack[-1][0] != '(':
                    self.out.append(self.stack.pop(-1)[0])
                if self.stack[-1][0] == '(':
                    self.stack.pop(-1)

        while len(self.stack) > 0:
            self.out.append(self.stack.pop(-1)[0])

    # RPN для условного оператора
    def if_expr(self, node):
        self.tokens.pop(0)
        buff_mi = copy.deepcopy(self.mi)
        self.assign_expr(generateTokenList(node.getNodes()[0].getNodes()[1], []))
        self.out.append('M' + str(buff_mi))
        self.out.append('false goto')
        self.mi = self.mi + 2
        for nodes1 in node.getNodes()[1].getNodes():
            for nodes2 in nodes1.getNodes():
                self.expr(nodes2)
        if len(node.getNodes()) > 2:
            self.out.append('M' + str(buff_mi+1))
            self.out.append('goto')
            self.out.append('M' + str(buff_mi) + ':')
            self.assign_expr(generateTokenList(node.getNodes()[3], [])[1:][:-1])
            self.out.append('M' + str(buff_mi+1) + ':')
        else:
            self.out.append('M' + str(buff_mi) + ':')


        # print(token_buff)
        None

    def while_expr(self, node):
        None

    def do_while_expr(self, node):
        None


# Использование дерева токенов для отделения выражений в блоки
def generateTokenList(tree, genTokenList):
    tab = ''
    if isinstance(tree.getParam(), tuple):
        genTokenList.append(tree.getParam())
    if len(tree.getNodes()) == 1:
        for l in tree.getNodes():
            generateTokenList(l, genTokenList)
    else:
        for l in tree.getNodes():
            generateTokenList(l, genTokenList)
    return genTokenList
