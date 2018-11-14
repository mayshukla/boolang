from Parser import BoolangParser
from Interpreter import Interpreter

def main():
    boolang_parser = BoolangParser()
    boolang_interpreter = Interpreter()
    
    #print(boolang_parser.parse('(a+b+c) (as+c(a+s)+df) (a+c)'))
    #print(boolang_parser.parse('0(z + b) + (a b+x (d) )1'))
    #print(boolang_parser.parse("x'y+(xy)''+(x+y)'"))

    my_ast = boolang_parser.parse(r"\def \f [x,y,z] {(x+z)'y+z}")
    print(my_ast)
    #boolang_interpreter.interpret(my_ast)
    
    # syntax error
    #print(boolang_parser.parse('x+'))


if __name__=='__main__':
    main()
