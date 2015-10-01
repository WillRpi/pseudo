import sys,lexer,tokens
f = open(sys.argv[1], "r", encoding="utf-8")
for o in lexer.lex(f.read()):
	print(o.toDict())
