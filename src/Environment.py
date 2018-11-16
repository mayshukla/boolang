from BoolangError import BoolangRuntimeError

class Environment:
    """ A class to store bindings of identifiers to values.
        Basically, a namespace.
    """

    # Dictionary where the keys are identifiers as plain strings,
    # values are the values associated with that identifier
    mappings = {}

    def __init__(self):
        # Start with no mappings
        self.mappings = {}

    def bind(self, identifier, value):
        """ Binds a new identifier or re-defines an old one
        """
        self.mappings[identifier] = value


    def lookup(self, identifier):
        """ Returns the value associated with identifier
            If identifier has not been bound yet, throws an error
        """
        try:
            return self.mappings[identifier]
        except KeyError:
            raise BoolangRuntimeError('boolang error: variable "{}" not defined'.format(identifier))
