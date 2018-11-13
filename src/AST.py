""" Define classes for all AST structures
"""


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
