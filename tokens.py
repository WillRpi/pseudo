import collections
# Token
class Token(collections.namedtuple('Token',('type','value'))):
    def toDict(self):
        return{'type':self.type,'value':self.value}
# Literals
class NumberLiteral(collections.namedtuple('NumberLiteral','value')):
    def toDict(self):
        return{'type':'NumberLiteral','value':self.value}
class StringLiteral(collections.namedtuple('StringLiteral','value')):
    def toDict(self):
        return{'type':'StringLiteral','value':self.value}
class NameLiteral(collections.namedtuple('NameLiteral','value')):
    def toDict(self):
        return{'type':'NameLiteral','value':self.value}
# Expressions
class UnaryOpExpression(collections.namedtuple('UnaryOpExpression',('op','value'))):
    def toDict(self):
        return{'type':'UnaryOpExpression','op':self.op.toDict(),'value':self.value.toDict()}
class BinaryOpExpression(collections.namedtuple('BinaryOpExpression',('op','prefix','postfix'))):
    def toDict(self):
        return{'type':'BinaryOpExpression','op':self.op.toDict(),'prefix':self.prefix.toDict(),'postfix':self.postfix.toDict()}
class Expression(collections.namedtuple('Expression','value')):
    def toDict(self):
        return{'type':'Expression','value':self.value.toDict()}
# Unary Operators
class USub():
    def toDict(self):
        return{'type':'USub'}
class Not():
    def toDict(self):
        return{'type':'Not'}
# Binary Operators
class Add():
    def toDict(self):
        return{'type':'Add'}
class Sub():
    def toDict(self):
        return{'type':'Sub'}
class Mult():
    def toDict(self):
        return{'type':'Mult'}
class Div():
    def toDict(self):
        return{'type':'Div'}
class Mod():
    def toDict(self):
        return{'type':'Mod'}
class Pow():
    def toDict(self):
        return{'type':'Pow'}
class UpShift():
    def toDict(self):
        return{'type':'UpShift'}
class DownShift():
    def toDict(self):
        return{'type':'DownShift'}
class BitOr():
    def toDict(self):
        return{'type':'BitOr'}
class BitXor():
    def toDict(self):
        return{'type':'BitXor'}
class BitAnd():
    def toDict(self):
        return{'type':'BitAnd'}
# Boolean Logic Operators (Binary)
class And():
    def toDict(self):
        return{'type':'And'}
class Or():
    def toDict(self):
        return{'type':'Or'}
# Booleans
class Compare(collections.namedtuple('Compare',('op','prefix','postfix'))):
    def toDict(self):
        return{'type':'Compare','op':self.op.toDict(),'prefix':self.prefix.toDict(),'postfix':self.postfix.toDict()}
# Boolean Compare Operators
class Eq():
    def toDict(self):
        return{'type':'Eq'}
class NotEq():
    def toDict(self):
        return{'type':'NotEq'}
class ObjEq():
    def toDict(self):
        return{'type':'ObjEq'}
class NotObjEq():
    def toDict(self):
        return{'type':'NotObjEq'}
class Lt():
    def toDict(self):
        return{'type':'Lt'}
class LtE():
    def toDict(self):
        return{'type':'LtE'}
class Gt():
    def toDict(self):
        return{'type':'Gt'}
class GtE():
    def toDict(self):
        return{'type':'GtE'}
# Variables
class Name(collections.namedtuple('Name',('name','ctx'))):
    def toDict(self):
        return{'type':'Name','name':self.name.toDict(),'ctx':self.ctx.toDict()}
# Attributes
class Attribute(collections.namedtuple('Attribute',('name','attr','ctx'))):
    def toDict(self):
        return{'type':'Attribute','name':self.var.toDict(),'attr':self.attr.toDict(),'ctx':self.ctx.toDict()}
# Subscripting
class Subscript(collections.namedtuple('Subscript',('name','index','ctx'))):
    def toDict(self):
        return{'type':'Attribute','Subscript':self.var.toDict(),'index':self.index.toDict(),'ctx':self.ctx.toDict()}
# Variable CTX types
class Load():
    def toDict(self):
        return{'type':'Load'}
class Store():
    def toDict(self):
        return{'type':'Store'}
class Del():
    def toDict(self):
        return{'type':'Del'}
# Functions
class Call(collections.namedtuple('Call',('name','args'))):
    def toDict(self):
        return{'type':'Call','name':self.name.toDict(),'args':self.args.toDict()}
# Logic
class IfExp(collections.namedtuple('IfExp',('test','body','elseBody'))):
    def toDict(self):
        return{'type':'IfExp','test':self.test.toDict(),'body':self.body.toDict(),'else':self.elseBody.toDict()}
