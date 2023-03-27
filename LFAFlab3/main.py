from lexer import Lexer
from scanner import Scanner
class Main:

    productions = {
        'S': ['aA', 'aB'],
        'A': ['bS'],
        'B': ['aC'],
        'C': ['a', 'bS'],
    }
    input_string = 'abbaba'

    lexer = Lexer(productions)
    tokens = lexer.tokenize(input_string)
    print(tokens)

    scanner = Scanner(productions)
    scanner.scan(input_string)
    print(scanner.scan(input_string))
    print("input is valid")



