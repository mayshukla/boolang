""" Custom error classes for boolang parser, syntax, runtime errors
"""

class BoolangError(Exception):
    """ Base class for all boolang errors
    """
    pass


class BoolangParserError(BoolangError):
    """ Exception for parser errors
    """

    #TODO: store line numbers
    def __init__(self, token):
        self.token = token
        self.message = 'Boolang parser error: Unexpected token "{}"'.format(self.token)


class BoolangSyntaxError(BoolangError):
    """ Exception for syntax errors
    """

    def __init__(self, token):
        self.token = token
        self.message = 'Boolang syntax error at "{}"'.format(self.token)


class BoolangRuntimeError(BoolangError):
    """ Exception for runtime errors
    """

    def __init__(self, message):
        # Since runtime errors can be diverse, this class just stores any
        # message
        self.message = message
