import re

def hackerrank_language(s):
    return re.findall(r'^[0-9]*[ ](C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$', s)
        
for _ in range(int(input())):
    if hackerrank_language(input()):
        print('VALID')
    else:
        print('INVALID')
