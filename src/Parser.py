from ply import lex, yacc
from AST import ExprAnd, ExprOr

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
        'SPACE',
        'LIT',
        'VAR',
        'PLUS',
        'LEFT_PAREN',
        'RIGHT_PAREN'
    ]


    # Define each token 
    #
    # note: lex recognizes tokens as variables that start with 't_'
    # note: raw strings are used to escape all backslashes and stuff in
    #       regular expressions.


    t_LIT = r'(0|1)'
    t_VAR = r'[a-zA-Z]'
    t_PLUS = r'\+'
    t_LEFT_PAREN = r'\('
    t_RIGHT_PAREN = r'\)'

    # String containing ignore characters
    #
    # note: in this case, a raw string is not used since we want an actual
    #       tab
    t_ignore = ' \t'


    def t_error(self, t):
        """ Called when lex meets a token which doesn't match any defined rules
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


    # We define grouping to include just VAR and LIT to make
    # the rule for "and" simpler
    #
    # This needs a separate function due to array index
    def p_grouping(self, p):
        """grouping : VAR
                    | LIT
        """
        p[0] = p[1]


    # Handle syntax errors
    def p_error(self, p):
        if p:
            raise Exception("Syntax error at '{}'".format(p.value))
        else:
            raise Exception("Syntax error at EOF")


    def parse(self, text):
        """ Parses text and returns AST
        """
        return yacc.parse(text)
