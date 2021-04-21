import Lexer
import Parser
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tokens = Lexer.join('test.txt')
    Parser.AST(tokens)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
