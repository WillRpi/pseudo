import lexer as l
f = open(sys.argv[1], "r", encoding="utf-8")
l.lex(f.read())
