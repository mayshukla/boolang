from ply import lex, yacc


"""

Declare list of all tokens for lex

"""
tokens = [
    'SPACE',
    'LIT',
    'VAR',
    'PLUS',
    'LEFT_PAREN',
    'RIGHT_PAREN'
]

""" 

Define each token 

note: lex recognizes tokens as variables that start with 't_'
note: raw strings are used to escape all backslashes and stuff in regular
      expressions.

"""
t_LIT = r'(0|1)'
t_VAR = r'[a-zA-Z]'
t_PLUS = r'\+'
t_LEFT_PAREN = r'\('
t_RIGHT_PAREN = r'\)'


# Truncate spaces down to one space
def t_SPACE(t):
    """\s+
    """
    t.value = ' '
    return t


def t_error(t):
    """ Called when lex meets a token which doesn't match any defined rules
    """
    raise TypeError('Error: unexpeced token "{}"'.format(t.value))


lex.lex()

"""

Parser rules

note: yacc recognizes parser rules as variables that start with 'p_'

"""

# Specify precedence and associativity of operators
# Top is highest precenence
precedence = [
    ('left', 'PLUS')
]


class ExprBinary:
    """Base class for a binary expression
    """
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __repr__(self):
        return "ExprBinary({}, {})".format(self.left, self.right)


class ExprOr(ExprBinary):
    """Derived class for an or expression
    """
    def __repr__(self):
        return "ExprOr({}, {})".format(self.left, self.right)


class ExprAnd(ExprBinary):
    """Derived class for an and expression
    """
    def __repr__(self):
        return "ExprAnd({}, {})".format(self.left, self.right)

    
def p_expr(p):
    """expr : or
            | and
            | grouping
            | VAR
            | LIT
    """
    p[0] = p[1]


def p_or(p):
    """or : expr PLUS expr
    """
    p[0] = ExprOr(p[1], p[3])


# Here we need a bunch of rules to catch every case since there is no
# "and" token
def p_and(p):
    """and : VAR VAR
           | VAR grouping
           | grouping VAR
           | grouping grouping
           | and VAR
           | and grouping
    """
    p[0] = ExprAnd(p[1], p[2]) 


def p_grouping(p):
    """grouping : LEFT_PAREN expr RIGHT_PAREN
    """
    p[0] = p[2]


yacc.yacc()


def main():
    #lex.input('01    10as dASDF+10')
    #for tok in iter(lex.token, None):
        #print(repr(tok.type), repr(tok.value))
    print(yacc.parse('(a+b+c)(as+c(a+s)+df)(a+c)'))


if __name__=='__main__':
    main()
