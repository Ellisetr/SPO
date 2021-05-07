import Lexer
import Parser
import RPN
import RPN
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Lexer = Lexer.Lexer('test2.txt')
    tokens = Lexer.startLexer()

    Parser = Parser.Parser(tokens)
    Parser.startParser()

    # RPN.rpn(tokens)

    RPN = RPN.RPN(Parser.getTree(), tokens)
    RPN.start()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
