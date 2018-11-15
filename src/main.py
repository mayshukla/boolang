from Parser import BoolangParser
from Interpreter import Interpreter

def main():
    boolang_parser = BoolangParser()
    boolang_interpreter = Interpreter()
    
    #print(boolang_parser.parse('(a+b+c) (as+c(a+s)+df) (a+c)'))
    #print(boolang_parser.parse('0(z + b) + (a b+x (d) )1'))
    #print(boolang_parser.parse("x'y+(xy)''+(x+y)'"))

    my_program = boolang_parser.parse(r"\def \f [x,y,z] {(x+z)'y+z}"
                                  + r"\truth \f"
                                  + r"\def \g [a,b] {a+b}"
                                  + r"\truth \g")

    boolang_interpreter.interpret(my_program)
    
    # syntax error
    #print(boolang_parser.parse('x+'))


if __name__=='__main__':
    main()
