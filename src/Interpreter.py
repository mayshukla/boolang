from AST import *
from BoolangObjects import *
from Environment import Environment
from BoolangError import BoolangRuntimeError


class Interpreter:
    globalEnvironment = Environment()

    def __init__(self):
        self.globalEnvironment = Environment()

    
    def interpret(self, program):
        """ Takes a Program from a BoolangParser and interprets it
        """

        for stmt in program.stmts:

            if isinstance(stmt, StmtDef):
                # Contruct a Boolang Function object
                function = Function(expr=stmt.expr,
                                    variable_list=stmt.variable_list)

                # Bind or re-bind a function identifier
                self.globalEnvironment.bind(stmt.identifier, function)

            elif isinstance(stmt, StmtTruth):
                # lookup that function in globalEnvironment and call
                # its truth() method
                self.globalEnvironment.lookup(stmt.identifier).truth()

            else:
                raise BoolangRuntimeError("Interpreter doesn't support that"
                                          + " type of statement yet.")
