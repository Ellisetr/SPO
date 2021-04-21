import re
import Lexer
"""""""""
lang -> expr+
expr -> assign_expr | if_expr | while_expr | do_while_expr

value -> NUMBER | VAR

if_expr -> if_head if_body (else_head else_body)?
if_head -> if_KW if_condition
if_condition -> L_BR logical_expr R_RB

logical_expr -> value (LOGICAL_OP value)*

if_body -> L_S_BR expr+ R_S_BR
else_body -> L_S_BR expr+ R_S_BR

while_expr -> while_head while_body
while_head -> while_KW logical_expression
while_body -> L_S_BR expr+ R_S_BR

do_while_expr -> do_KW do_while_body
do_while_body -> L_S_BR expr+ R_S_BR while_kw logical_expr

assign_expr -> VAR ASSIGN_OP value_expr*
value_expr -> (value_expr_brackets | value) (OP value_expr)?
value_expr_brackets -> L_BR value_expr R_BR
"""""
token_list = [[], []]


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



def lang():
    node = Node('lang')
    while len(token_list) > 0:
        node.addNode(expr())
    return node


def expr():
    node = Node('expr')
    if token_list[0][0] == 'VAR':
         node.addNode(assign_expr())
    elif token_list[0][0] == 'if_KW':
         node.addNode(if_expr())
    elif token_list[0][0] == 'while_KW':
        node.addNode(while_expr())
    elif token_list[0][0] == 'do_KW':
        node.addNode(do_while_expr())
    return node



# IF_EXPR
def if_expr():
    node = Node('if_expr')
    node.addNode(if_head())
    node.addNode(body('if_KW'))
    try:
        node.addNode(match('else_KW'))
        node.addNode(body('else_KW'))
    except Exception:
        print('No else found')
    return node


def if_head():
    node = Node('if_head')
    node.addNode(match('if_KW'))
    node.addNode(if_condition())
    return node


def if_condition():
    node = Node('if_condition')
    node.addNode(match('L_BR'))
    node.addNode(logical_expr())
    node.addNode(match('R_BR'))
    return node

def match(input_str):
    node = Node(token_list[0])
    if (input_str == token_list[0][0]):
        token_list.pop(0)
        return node
    else: raise Exception('Unknown symbol' + token_list[0][0])

def body(KW):
    node = Node(KW)
    node.addNode(match('L_S_BR'))
    node.addNode(expr())
    while re.match('(VAR)|(if_KW)|(while_KW)', token_list[0][0]):
        node.addNode(expr())
    node.addNode(match('R_S_BR'))
    return node

# WHILE_EXPR
def while_expr():
    node = Node('while_expr')
    node.addNode(while_head())
    node.addNode(body('while_body'))
    return node

def while_head():
    node = Node('while_head')
    node.addNode(match('while_KW'))
    node.addNode(match('L_BR'))
    node.addNode(logical_expr())
    node.addNode(match('R_BR'))
    return node

# ASSIGN_EXPR
def assign_expr():
    node = Node('assign_expr')
    node.addNode(match('VAR'))
    node.addNode(match('ASSIGN_OP'))
    node.addNode(value_expr())
    return node


def value_expr():
    node = Node('value_expr')
    err = ''
    try:
        node.addNode(value_expr_brackets())
    except Exception:
        err= err+'Error'

    try:
        node.addNode(value())
    except Exception:
        err = err + ' Found'

    try:
        node.addNode(match('OP'))
        node.addNode(value_expr())
    except Exception:
        None

    if (err == 'Error Found'):
        raise Exception('Error')

    return node


def value_expr_brackets():
    node = Node('value_expr_brackets')
    node.addNode(match('L_BR'))
    node.addNode(value_expr())
    node.addNode(match('R_BR'))
    return node


# LOGICAL_EXPR
def logical_expr():
    node = Node('logical_expr')
    node.addNode(value())
    node.addNode(match('LOGICAL_OP'))
    node.addNode(value())
    return node

def do_while_expr():
    node = Node('do_while_expr')
    node.addNode(match('do_KW'))
    node.addNode(do_while_body())
    return node

def do_while_body():
    node = Node('do_while_body')
    node.addNode(body(''))
    node.addNode(match('while_KW'))
    node.addNode(match('L_BR'))
    node.addNode(logical_expr())
    node.addNode(match('R_BR'))
    return node

def value():
    node = Node('VALUE')
    if token_list[0][0] == 'NUMBER':
        node.addNode(match('NUMBER'))
        return node
    elif token_list[0][0] == 'VAR':
        node.addNode(match('VAR'))
        return node
    else: raise Exception('Unknown symbol' + token_list[0][0])


def AST(tokens):
    global token_list
    token_list = tokens
    root = lang()
    print('Print AST')
    printAST(root, 0)


def parser():
    None

def printAST(tree, level):
    tab = ''
    for i in range (level):
        tab = tab+'     '
    print(tab, tree.getParam())

    for l in tree.getNodes():
        printAST(l, level+1)
