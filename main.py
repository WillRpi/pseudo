import sys,lexer
f = open(sys.argv[1], "r", encoding="utf-8")
lexer.lex(f.read())
