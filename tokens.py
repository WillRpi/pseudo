class IntegerLiteral(collections.namedtuple('IntegerLiteral','value')):
    def toDict(self):
        return{'type':'IntegerLiteral','value':self.value}
class UnaryOpExpression(collections.namedtuple('UnaryOpExpression',('op','value'))):
    def toDict(self):
        return{'type':'UnaryOpExpression','op':self.op,'value':self.value}
class BinaryOpExpression(collections.namedtuple('BinaryOpExpression',('op','prefix','postfix'))):
    def toDict(self):
        return{'type':'BinaryOpExpression','op':self.op,'prefix':self.prefix,'postfix':self.postfix}
