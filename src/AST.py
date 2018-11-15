""" Define classes for all AST structures
"""

from Environment import Environment

#TODO: add evaluate(environment) methods to every structure


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
    """ Derived class for a boolean variable name
    """
    def __repr__(self):
        return "ExprVariable({})".format(self.value)


    def evaluate(self, enviroment):
        return enviroment.lookup(self.value)

    
class ExprLiteral(ExprIdentifier):
    """ Derived class for a literal
    """
    def __repr__(self):
        return "ExprLiteral({})".format(self.value)


    def evaluate(self, enviroment):
        # The value of an ExprLiteral is '0' or '1'
        if self.value == '0':
            return False
        else:
            return True


class ExprNot(ExprUnary):
    """ Derived class for a unary not expression
    """
    def __repr__(self):
        return "ExprNot({})".format(self.value)


    def evaluate(self, environment):
        # takes environment as an argument for the sake of a consistent interface
        return not self.value.evaluate(environment)


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


    def evaluate(self, environment):
        return self.left.evaluate(environment) or self.right.evaluate(environment)


class ExprAnd(ExprBinary):
    """ Derived class for an and expression
    """
    def __repr__(self):
        return "ExprAnd({}, {})".format(self.left, self.right)


    def evaluate(self, environment):
        return self.left.evaluate(environment) and self.right.evaluate(environment)


#TODO: base class for Stmt?
#TODO: program class? a list of Stmt's?

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


class StmtTruth:
    """ Class for \truth statments
    """

    # the name of the function we want to print the truth table of
    identifier = ''

    def __init__(self, identifier):
        self.identifier = identifier
    def __repr__(self):
        return "StmtTruth('{}')".format(self.identifier)


class Program:
    """ Wrapper class to hold a flat list of statements
    """

    stmts = []

    def __init__(self):
        self.stmts = []


    def __repr__(self):
        return "Program({})".format(self.stmts)
    

    def add_stmt(self, stmt):
        self.stmts = self.stmts + [stmt]
