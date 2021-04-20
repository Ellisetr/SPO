"""""""""
lang -> expr+
expr -> assign_expr | if_expr | while_expr | do_while_expr

value -> NUMBER | VAR

if_expr -> if_head if_body (else_head else_body)?
if_head -> if_KW if_condition
if_condition -> L_BR logical_expression R_RB

logical_expression -> value (LOGICAL_OP value)*

if_body -> L_S_BR expr+ R_S_BR
else_body -> L_S_BR expr+ R_S_BR

while_expr -> while_head while_body
while_head -> while_KW logical_expression
while_body -> L_S_BR expr+ R_S_BR

do_while_expr -> do_KW do_while_body
do_while_body -> L_S_BR expr+ R_S_BR while_kw logical_expression

assign_expr -> VAR ASSIGN_OP value_expr*
value_expr -> (value_expr_brackets | value) (OP value_expr)?
value_expr_brackets -> L_BR value_expr R_BR
"""""


class Node:
    def __init__(self, parent):
        self.parent = parent
        self.node = []

    def addNode(self, node):
        self.node.append(node)

    def printNode(self):
        for nodes in self.node:
            print(nodes)

    def getNode(self):
        return self.node

    def getParent(self):
        return self.parent


def validator(tokens):
    print('test')
