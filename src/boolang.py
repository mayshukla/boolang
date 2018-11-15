""" This is the main module for boolang
"""


import sys

from Parser import BoolangParser
from Interpreter import Interpreter


def repl():
    parser = BoolangParser()
    interpreter = Interpreter()

    print('Welcome to the boolang REPL!')

    while True:
        line = input('> ')

        program = parser.parse(line)
        interpreter.interpret(program)


def interpret_file(filename):
    parser = BoolangParser()
    interpreter = Interpreter()

    text = ''
    try:
        with open(filename) as f:
            # read entire file
            text = f.read()
    except FileNotFoundError:
        print('Error: file not found.')
        sys.exit(1)

    program = parser.parse(text)
    interpreter.interpret(program)


def main():
    if len(sys.argv) == 1:
        repl()

    elif len(sys.argv) == 2:
        interpret_file(sys.argv[1])

    else:
        print('Usage: boolang [source file]')



if __name__=='__main__':
    main()
