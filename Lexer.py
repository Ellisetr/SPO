import re

terminals = \
    [
        ('if_KW', '^(if)$', 1),
        ('else_KW', '^(else)$', 1),
        ('while_KW', '^(while)$', 1),
        ('do_KW', '^(do)$', 1),
        ('VAR', '^[a-zA-Z]{1}[a-zA-Z_0-9]{0,}$', 0),
        ('NUMBER', '^0|[1-9][0-9]*$', 0),
        ('ASSIGN_OP', '^=$', 0),
        ('OP', '^(\+|\-|\*|\/)$', 0),
        ('L_BR', '^\($', 0),
        ('R_BR', '^\)$', 0),
        ('L_S_BR', '^{$', 0),
        ('R_S_BR', '^}$', 0),
        ('WS',' ',0),
        ('LOGICAL_OP', '^((and)|(or)|(xor)|(nor)|(==)|(!=)|(>)|(>=)|(<)|(<=))$', 0)
    ]


def join(file):
    data = open(file).read().replace('\n', ' ')
    tokens = lexer_start(data)
    print(tokens)
    #print(Parser.parse_AST(tokens))


def lexer_start(input_string):
    lexemes = []
    while len(input_string) > 0:
        buff = lexer(input_string)[:2]
        if buff[0] != 'WS':
            lexemes.append(buff)
        input_string = input_string[lexer(input_string)[3]:]
    return lexemes


def lexer(input_string):
    buffer = ''
    buffer += input_string[0]
    if len(matcher(buffer)) > 0:
        while len(matcher(buffer)) > 0 and len(buffer) < len(input_string):
            buffer += input_string[len(buffer)]
        if len(buffer) > 1:
            buffer = buffer[:len(buffer) - 1]
        return max(matcher(buffer))
    else:
        raise Exception('Unknown symbol ' + buffer)


def matcher(buffer):
    matches = []
    for terminal in terminals:
        match = re.fullmatch(terminal[1], buffer)
        if match is not None:
            matches.append((terminal[0], match.string, terminal[2], match.endpos))
    return matches
