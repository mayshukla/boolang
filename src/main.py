from Parser import BoolangParser

def main():
    boolangParser = BoolangParser()
    
    print(boolangParser.parse('(a+b+c) (as+c(a+s)+df) (a+c)'))
    print(boolangParser.parse('0(z + b) + (a b+x (d) )1'))
    print(boolangParser.parse("x'y+(xy)''+(x+y)'"))
    # syntax error
    #print(boolangParser.parse('x+'))


if __name__=='__main__':
    main()
