import ply.lex as lex

tokens = [
    'KEYWORD',
    'SYMBOL',
    'INTEGER',
    'STRING',
    'IDENTIFIER'
]

t_KEYWORD = r"blueprint | def | method | field | static | var | int | char | boolean | void | true | false | null | this | if | elif | else | while | return |  prompt | valid_values"
t_SYMBOL = r" { | } | \[ | \] | \( | \) | . | , | ; | : | \+ | - | \* | / | < | > | = | ~"
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t 
t_STRING = r"\".*\""
t_IDENTIFIER= r"[a-zA-Z]([A-Za-z0-9])*"

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def test(data):
        lexer.input(data)
        while True:
             tok = lexer.token()
             if not tok:
                 break
             print(tok)


