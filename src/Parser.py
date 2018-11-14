from ply import lex, yacc
from AST import *

alpha = "abcdefghijklmnopqrstuvwxyz"

class Parser:
    """ Base class for lexer/parser 
    """

    tokens = []
    precedence = []

    def __init__(self):
        # Build the lexer and parser from the variables and methods
        # of the current object
        lex.lex(module=self)
        yacc.yacc(module=self)


class BoolangParser(Parser):
    """ Defines all token and syntax rules for boolang
    """

    # Declare list of tokens for lex
    tokens = [
        'TICK',
        'LIT',
        'VAR',
        'PLUS',
        #'COMMA',
        'LEFT_PAREN',
        'RIGHT_PAREN',
        #'LEFT_BRACKET',
        #'RIGHT_BRACKET',
        'LEFT_BRACE',
        'RIGHT_BRACE',

        # for variable lists in function definitions and
        # passing arguments in evalution statements
        'LIST',

        # generic identifier
        'IDENTIFIER'
    ]

    # Reserved keywords and their corresponding token types
    reserved = {
        r'\def':'DEF',
        r'\truth':'TRUTH'
    }
    tokens = tokens + list(reserved.values())


    # Define each token 
    #
    # note: lex recognizes tokens as variables that start with 't_'
    # note: raw strings are used to escape all backslashes and stuff in
    #       regular expressions.


    t_TICK = r"'"
    t_LIT = r'(0|1)'
    t_VAR = r'[a-zA-Z]'
    t_PLUS = r'\+'
    #t_COMMA = r'\,'
    t_LEFT_PAREN = r'\('
    t_RIGHT_PAREN = r'\)'
    #t_LEFT_BRACKET = r'\['
    #t_RIGHT_BRACKET = r'\]'
    t_LEFT_BRACE = r'\{'
    t_RIGHT_BRACE = r'\}'


    # String containing ignore characters
    #
    # note: in this case, a raw string is not used since we want an actual
    #       tab
    t_ignore = ' \t'


    # Handle indentifiers, including reserved keywords
    #
    # An identifier is a backslash followed by one or more letters or
    # underscores
    def t_IDENTIFIER(self, t):
        r'\\[a-zA-Z_]+'

        # Check if the identifier is a reserved keyword
        #
        # If not in reserved, it is just a generic identifier
        t.type = self.reserved.get(t.value, 'IDENTIFIER')

        # Strip leading backslash
        t.value = t.value[1:]

        return t


    # Matches something like [x, y, z]
    # store only a list ['x','y','z']
    def t_LIST(self, t):
        r'\[\s*([a-zA-Z])\s*(,\s*([a-zA-Z])\s*)*\]'

        raw_list = t.value
        t.value = []

        # Extract only the contents of the list
        # By this point, that should be any alphabetical or 0 or 1
        for char in raw_list:
            if char in alpha or char in '01':
                t.value += char

        return t


    def t_error(self, t):
        """ Called when lex meets a token which doesn't match any defined 
            rules
        """
        raise TypeError('Error: unexpeced token "{}"'.format(t.value))


    # Define parser rules
    #
    # note: yacc recognizes parser rules as variables that start with 'p_'

    # Specify precedence and associativity of operators
    # Top is highest precenence
    precedence = [
        ('left', 'PLUS')
    ]


    # TODO: a statement can also be a truth statement
    def p_stmt(self, p):
        """stmt : def
        """
        p[0] = p[1]


    def p_def(self, p):
        """def : DEF IDENTIFIER LIST LEFT_BRACE expr RIGHT_BRACE
        """
        p[0] = StmtDef(identifier=p[2],
                       variable_list=p[3],
                       expr=p[5])


    def p_expr(self, p):
        """expr : or
                | and
                | grouping
        """
        p[0] = p[1]


    def p_or(self, p):
        """or : expr PLUS expr
        """
        p[0] = ExprOr(p[1], p[3])


    # We need to define 2 rules for "and" since there is no "and" token
    #
    # Otherwise we'd just go "and : expr AND expr"
    def p_and(self, p):
        """and : grouping grouping
               | and grouping
        """
        p[0] = ExprAnd(p[1], p[2]) 


    def p_paren_grouping(self, p):
        """grouping : LEFT_PAREN expr RIGHT_PAREN
        """
        p[0] = p[2]


    # Define unary negation (e.g. " x' ") as another type of grouping
    def p_not(self, p):
        """grouping : grouping TICK
        """
        p[0] = ExprNot(p[1])


    # We define grouping to include just VAR and LIT to make
    # the rule for "and" simpler
    #
    # This needs a separate function due to array index
    def p_variable(self, p):
        """grouping : VAR
        """
        p[0] = ExprVariable(p[1])
    def p_literal(self, p):
        """grouping : LIT
        """
        p[0] = ExprLiteral(p[1])


    # Handle syntax errors
    def p_error(self, p):
        if p:
            raise Exception("Syntax error at '{}'".format(p.value))
        else:
            raise Exception("Syntax error at EOF")


    def print_tokens(self, text):
       """ Only does the lexing part and prints the result. 
           Useful for debugging only
       """

       lex.input(text)

       while True:
           tok = lex.token()
           if not tok: 
               break      # No more input
           print(tok)

       

    def parse(self, text):
        """ Parses text and returns AST
        """
        return yacc.parse(text)
