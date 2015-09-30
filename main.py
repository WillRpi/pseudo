cmd=input()
args=cmd.split()
if(args[0]=="read"):
    f = open(args[1], "r", encoding="utf-8")
    lex(f.read())
