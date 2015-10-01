import io,collections,tokens
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
def lex(string):
    operatorTokens=frozenset("=><+-/*!%&|");
    abcTokens=frozenset("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    abcNTokens=frozenset("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
    nTokens=frozenset("1234567890")
    sTokens=frozenset("(){},")
    token=""
    tokenClass=0
    tokenModifier=0
    readMode=0
    tokenArray=[]
    for i in range(0,len(string)):
        if(readMode==0):
            if(tokenClass!=0):
                if(tokenClass==1):
                    if(string[i] in operatorTokens):
                        token+=string[i]
                    else:
                        tokenArray.append(tokens.Token(tokenClass,token))
                        tokenClass=0
                elif(tokenClass==2):
                    if(string[i] in abcNTokens):
                        token+=string[i]
                    else:
                        tokenArray.append(tokens.Token(tokenClass,token))
                        tokenClass=0
                elif(tokenClass==3):
                    if(string[i] in nTokens):
                        token+=string[i]
                    else:
                        tokenArray.append(tokens.Token(tokenClass,token))
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
                    tokenArray.append(tokens.Token(4,string[i]))
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
                tokenArray.append(tokens.Token(tokenClass,token))
                tokenClass=0
                readMode=0
            elif(string[i]=="'"and tokenModifier==0):
                tokenArray.append(tokens.Token(tokenClass,token))
                tokenClass=0
                readMode=0
            else:
                token+=string[i]
    return tokenArray;
