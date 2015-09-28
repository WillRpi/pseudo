import io,collections;
#   Token Class Guide
#
#   0: None
#   1: Operator
#   2: Name
#   3: Number
#   4: Symbol
#   5: String
#       0: Single Quote Modifier
#       1: Double Quote Modifier
#
#   Read Mode Guide
#
#   0: Regular
#   1: String
#
operatorTokens=frozenset("=><+-/*!%&|");
abcTokens=frozenset("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
abcNTokens=frozenset("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
nTokens=frozenset("1234567890")
sTokens=frozenset("(){},")
def tokenTypeToName(tokenType):
    rv=""
    if(tokenType==0):
        rv="[none]"
    elif(tokenType==1):
        rv="[operator]"
    elif(tokenType==2):
        rv="[name]"
    elif(tokenType==3):
        rv="[number]"
    elif(tokenType==4):
        rv="[symbol]"
    elif(tokenType==5):
        rv="[string]"
    return rv;
class t:
    tokenType=0
    tokenValue=""
    def __init__(self,tokenType,tokenValue):
        self.tokenType=tokenType
        self.tokenValue=tokenValue
    def getTokenType(self):
        return self.tokenType
    def getTokenValue(self):
        return self.tokenValue
class IntegerLiteral(collections.namedtuple('IntegerLiteral','value')):
    def toDict(self):
        return{'type':'IntegerLiteral','value':self.value}
class UnaryOpExpression(collections.namedtuple('UnaryOpExpression',('op','value'))):
    def toDict(self):
        return{'type':'UnaryOpExpression','op':self.op,'value':self.value}
class BinaryOpExpression(collections.namedtuple('BinaryOpExpression',('op','prefix','postfix'))):
    def toDict(self):
        return{'type':'BinaryOpExpression','op':self.op,'prefix':self.prefix,'postfix':self.postfix}
print(BinaryOpExpression("+",IntegerLiteral(3),IntegerLiteral(3)))
class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self, item):
        self.items.append(item)
    def peek(self):
       return self.items[len(self.items)-1]
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
class CycleStack:
    def __init__(self,items):
        self.items=list(items)
        self.cursor=0
        self.cursorStack=[]
    def isEmpty(self):
        return self.items==[]
    def push(self, item):
        self.items.append(item)
    def peek(self):
       try:
           return self.items[selfCursor]
       except IndexError:
           print("unexpected end of input")
    def pop(self):
        rv=self.peek()
        self.cursor++
        return rv
    def pushCursor(self):
        self.cursorStack.append(self.cursor)
    def popCursor(self):
        self.cursor=self.cursorStack.pop()
    def size(self):
        return len(self.items)
def lex(string):
    token=""
    tokenClass=0
    tokenModifier=0
    readMode=0
    tokens=[]
    for i in range(0,len(string)):
        if(readMode==0):
            if(tokenClass!=0):
                if(tokenClass==1):
                    if(string[i] in operatorTokens):
                        token+=string[i]
                    else:
                        tokens.append(t(tokenClass,token))
                        tokenClass=0
                elif(tokenClass==2):
                    if(string[i] in abcNTokens):
                        token+=string[i]
                    else:
                        tokens.append(t(tokenClass,token))
                        tokenClass=0
                elif(tokenClass==3):
                    if(string[i] in nTokens):
                        token+=string[i]
                    else:
                        tokens.append(t(tokenClass,token))
                        tokenClass=0
            if(tokenClass==0):
                token="";
                if(string[i] in operatorTokens):
                    token+=string[i]
                    tokenClass=1
                elif(string[i] in abcTokens):
                    token+=string[i]
                    tokenClass=2
                elif(string[i] in nTokens):
                    token+=string[i]
                    tokenClass=3
                elif(string[i] in sTokens):
                    tokens.append(t(4,string[i]))
                elif(string[i]=="\""):
                    tokenClass=5
                    tokenModifier=1
                    readMode=1
                elif(string[i]=="'"):
                    tokenClass=5
                    tokenModifier=0
                    readMode=1
        elif(readMode==1):
            if(string[i]=="\""and tokenModifier==1):
                tokens.append(t(tokenClass,token))
                tokenClass=0
                readMode=0
            elif(string[i]=="'"and tokenModifier==0):
                tokens.append(t(tokenClass,token))
                tokenClass=0
                readMode=0
            else:
                token+=string[i]
    return tokens;
def parse(tokens):
    
cmd=input()
args=cmd.split()
if(args[0]=="read"):
    f = open(args[1], "r", encoding="utf-8")
    lex(f.read())
