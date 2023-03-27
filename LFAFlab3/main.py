from lexer import Lexer
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
    print('tokenized string')
    print(tokens)
    print("input is valid")



