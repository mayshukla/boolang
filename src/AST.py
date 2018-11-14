""" Define classes for all AST structures
"""


class Expr:
    """ Base class for all expressions
    """
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return "Expr({})".format(self.value)


class ExprUnary(Expr):
    """ Base class for a unary expression
    """
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return "ExprUnary({})".format(self.value)


class ExprIdentifier(ExprUnary):
    """ Derived class for an identifier
    """
    def __repr__(self):
        return "ExprIdentifier({})".format(self.value)


class ExprVariable(ExprIdentifier):
    """ Derived class for an identifier such as a variable name
    """
    def __repr__(self):
        return "ExprVariable({})".format(self.value)

    
class ExprLiteral(ExprIdentifier):
    """ Derived class for a literal
    """
    def __repr__(self):
        return "ExprVariable({})".format(self.value)


class ExprNot(ExprUnary):
    """ Derived class for a unary not expression
    """
    def __repr__(self):
        return "ExprNot({})".format(self.value)


class ExprBinary(Expr):
    """ Base class for a binary expression
    """
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __repr__(self):
        return "ExprBinary({}, {})".format(self.left, self.right)


class ExprOr(ExprBinary):
    """ Derived class for an or expression
    """
    def __repr__(self):
        return "ExprOr({}, {})".format(self.left, self.right)


class ExprAnd(ExprBinary):
    """ Derived class for an and expression
    """
    def __repr__(self):
        return "ExprAnd({}, {})".format(self.left, self.right)


#TODO: base class for Stmt?

class StmtDef:
    """ Class for all function definition statments
    """

    identifier = ''    # the identifier to bind the function to
    variable_list = [] # a list of all the variables
    expr = Expr        # the actual expression of the function

    def __init__(self, **kwargs):
        self.identifier = kwargs['identifier']
        self.variable_list = kwargs['variable_list']
        self.expr = kwargs['expr']
    def __repr__(self):
        return "StmtDef(identifier={}, variable_list={}, expr={})".format(
            self.identifier, self.variable_list, self.expr)
