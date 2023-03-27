from lexer import Lexer
from scanner import Scanner
class Main:

    productions = {
        'S': ['aA', 'aB'],
        'A': ['bS'],
        'B': ['aC'],
        'C': ['a', 'bS'],
    }
    input_string = 'AabSababa'
    scanner_string = 'abbaba'
    lexer = Lexer(productions)
    tokens = lexer.tokenize(input_string)
    print(tokens)

    scanner = Scanner(productions)
    scanner.scan(scanner_string)
    print(scanner.scan(scanner_string))



