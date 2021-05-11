import re

terminals = \
    [
        ('if_KW', '^(if)$', 1),
        ('else_KW', '^(else)$', 1),
        ('while_KW', '^(while)$', 1),
        ('do_KW', '^(do)$', 1),
        ('VAR', '^-?[a-zA-Z]{1}[a-zA-Z_0-9]{0,}$', 0),
        ('NUMBER', '^0|-?[1-9][0-9]*$', 0),
        ('ASSIGN_OP', '^=$', 0),
        ('OP', '^(\+|\-|\*|\/)$', 0),
        ('L_BR', '^\($', 0),
        ('R_BR', '^\)$', 0),
        ('L_S_BR', '^{$', 0),
        ('R_S_BR', '^}$', 0),
        ('WS', ' ', 0),
        ('LOGICAL_OP', '^((&)|(||)|(xor)|(nor)|(==)|(!=)|(>)|(>=)|(<)|(<=))$', 0),
        ('print_KW', '^(print)$', 1),
        ('remove_KW', '^(remove)$', 1),
        ('put_KW', '^(put)$', 1),
        ('clear_KW', '^(clear)$', 1),
        ('size_KW', '^(size)$', 1),
        ('get_KW', '^(get)$', 1),
        ('is_empty_KW', '^(isEmpty)$', 1),
        ('contains_KW', '^(clear)$', 1),
        ('hashmap_KW', '^(hashMap)$', 1),
    ]


class Lexer:
    def __init__(self, file):
        print('Input file:')
        print(open(file).read())
        self.data = open(file).read().replace('\n', ' ')
        self.tokens = [[], []]

    def startLexer(self):
        print('Lexer:')
        tokens = self.nextLexeme(self.data)
        print(tokens)
        return tokens

    def nextLexeme(self, input_string):
        tokens = []
        while len(input_string) > 0:
            buffer = self.lexeme(input_string)
            input_string = input_string[len(buffer[1]):]
            if buffer[0] != 'WS':
                tokens.append(buffer[:2])
        return tokens

    def lexeme(self, input_string):
        buffer = ''
        buffer += input_string[0]
        if len(self.matcher(buffer)) > 0:
            while len(self.matcher(buffer)) > 0 and len(buffer) < len(input_string):
                buffer += input_string[len(buffer)]
            if len(buffer) > 1:
                buffer = buffer[:len(buffer) - 1]
            return max(self.matcher(buffer))
        else:
            raise Exception('Unknown symbol ' + buffer)

    def matcher(self, buffer):
        matches = []
        for terminal in terminals:
            match = re.fullmatch(terminal[1], buffer)
            if match is not None:
                matches.append((terminal[0], match.string, terminal[2]))
        return matches
