# Lexer & Scanner
## Course: Formal Languages & Finite Automata
## Author: Nistor Stefan FAF-211
Variant 18

VN={S, A, B, C}, 

VT={a, b}, 

P={ 
    S → aA     
    A → bS    
    S → aB   
    B → aC    
    C → a  
    C → bS
}


## Theory
    The term lexer comes from lexical analysis which, in turn, represents the process of extracting lexical tokens from a string of characters. There are several alternative names for the mechanism called lexer, for example tokenizer or scanner. The lexical analysis is one of the first stages used in a compiler/interpreter when dealing with programming, markup or other types of languages.     The tokens are identified based on some rules of the language and the products that the lexer gives are called lexemes. So basically the lexer is a stream of lexemes. Now in case it is not clear what's the difference between lexemes and tokens, there is a big one. The lexeme is just the byproduct of splitting based on delimiters, for example spaces, but the tokens give names or categories to each lexeme. So the tokens don't retain necessarily the actual value of the lexeme, but rather the type of it and maybe some metadata.

## Objectives:
- Understand what lexical analysis [1] is.

- Get familiar with the inner workings of a lexer/scanner/tokenizer.

- Implement a sample lexer and show how it works.
  

## Implementation description
### Lexer class
This code defines a lexer class that takes a set of production rules as input and extracts the terminal symbols from them. It provides a tokenize method that takes an input string and produces a list of tokens, where each token is a tuple consisting of a type ('TERMINAL' for lowercase letters and 'NON_TERMINAL' for uppercase letters) and the actual symbol. The tokenize method loops over the input string, identifies each character as a terminal or non-terminal symbol based on whether it is a lowercase or uppercase letter, respectively, and adds it to the list of tokens. If the character is neither a lowercase nor an uppercase letter, the input is invalid and an exception is raised.

```python

class Lexer:
    # Initialize the lexer with the production rules
    def __init__(self, productions):
        self.productions = productions
        self.start_symbol = 'S'
        terminals = set()
        # Loop over the production rules to extract the terminals
        for value in productions.values():
            # If the production rule is a string, extract the lowercase letters
            if isinstance(value, str):
                terminals.update(re.findall(r'[a-z]', value))
            # If the production rule is a list of strings, join them together first and then extract the lowercase letters
            else:
                terminals.update(re.findall(r'[a-z]', ''.join(value)))
        self.terminals = terminals

    # Tokenize an input string
    def tokenize(self, input_string):
        tokens = []
        i = 0
        # Loop over the input string
        while i < len(input_string):
            # If the current character is a lowercase letter, it is a terminal symbol
            match = re.match(r'[a-z]', input_string[i])
            if match:
                tokens.append(('TERMINAL', match.group()))
                i += 1
            # If the current character is an uppercase letter, it is a non-terminal symbol
            else:
                match = re.match(r'[A-Z]', input_string[i])
                if match:
                    tokens.append(('NON_TERMINAL', match.group()))
                    i += 1
                # If the current character is neither a lowercase nor an uppercase letter, the input is invalid
                else:
                    raise ValueError('Invalid input')
        return tokens
```
### Scanner class
The Scanner class is designed to take in a dictionary of production rules and extract all of the terminal symbols from those rules. The self.terminals attribute is then set to be a set of all terminal symbols. When the scan method is called with an input string, the method loops over the input string and attempts to match the input with one of the terminal symbols. If a match is found, the method adds a tuple to the tokens list that contains the type of the token ('TERMINAL') and the matched string. The input string is then shortened by the length of the matched string, and the loop continues. If no match is found, an error is raised. The scan method then returns the list of tokens that it has generated. Overall, this code provides a way to tokenize an input string based on the production rules and terminal symbols specified in a dictionary.

```python
    class Scanner:
    def __init__(self, productions):
        self.productions = productions
        self.start_symbol = 'S'

        # Extract all terminals from the productions
        self.terminals = set()
        for production in productions.values():
            if isinstance(production, list):
                for p in production:
                    # If production is a list, join its elements into a single string
                    # and extract terminals from it
                    self.terminals.update(re.findall(r'[a-z]', ''.join(p)))
            else:
                self.terminals.update(re.findall(r'[a-z]', production))

    def scan(self, input_string):
        tokens = []
        while input_string:
            matched = False
            # Sort the terminals in decreasing order of length, to match longer terminals first
            for terminal in sorted(self.terminals, key=lambda x: len(x), reverse=True):
                if input_string.startswith(terminal):
                    tokens.append(('TERMINAL', terminal))
                    input_string = input_string[len(terminal):]
                    matched = True
                    break

            if not matched:
                # If no terminal matches, raise an error
                raise ValueError('Invalid input')

        return tokens
```

### Main

```python
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
```



## Results
![Alt text](C:\Users\snist\OneDrive\Desktop\LFAFlabs\LFAFlab3\report and source code/screens/Screenshot_1.jpg)
## Conclusions
In this project, we implemented a lexer and a scanner using regular expressions in Python. The lexer is responsible for tokenizing an input string and identifying the terminal and non-terminal symbols present in it based on a set of production rules. The scanner, on the other hand, is responsible for extracting all terminal symbols from the production rules and scanning an input string to identify and tokenize the longest matching terminals. The scanner and lexer are important tools in programming language processing and can be used for tasks such as syntax highlighting, code completion, and program analysis. Overall, this project provides a good foundation for understanding and implementing lexers and scanners in Python.