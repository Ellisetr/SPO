import Lexer
import TuringMachine
import Parser
import RPN


if __name__ == '__main__':
    Lexer = Lexer.Lexer('hashmap_doublell_test.txt') # Указать название файла с кодом
    tokens = Lexer.startLexer()

    Parser = Parser.Parser(tokens)
    Parser.startParser()

    RPN = RPN.RPN(Parser.getTree(), tokens)
    RPN.start()

    TuringMachine = TuringMachine.Turing(RPN.getStack())
    TuringMachine.start()


