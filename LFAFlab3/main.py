from lexer import Lexer
class Main:
    lexer = Lexer()
    tokens = lexer.tokenize("2 + 3 * (4 - 1)")
    print(tokens)
    print('input valid')


