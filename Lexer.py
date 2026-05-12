import ply.lex as lex

reserved = {
        "blueprint":"BLUEPRINT",
        "def":"DEF",
        "method":"METHOD",
        "field":"FIELD",
        "static":"STATIC",
        "var":"VAR",
        "int":"INT",
        "char":"CHAR",
        "boolean":"BOOLEAN",
        "void":"VOID",
        "true":"TRUE",
        "false":"FALSE",
        "null":"NULL",
        "this":"THIS",
        "if":"IF",
        "elif":"ELIF",
        "else":"ELSE",
        "while":"WHILE",
        "return":"RETURN",
        "prompt":"PROMPT",
        "valid_values":"VALID_VALUES"
        }

tokens = [
    'COMMENT',
    'INTEGER',
    'STRING',
    'IDENTIFIER'
] + list(reserved.values())
literals = ["{","}","[","]","(",")",".",",",";",":","+","-","*","/","<",">","=","~"]


def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t 

t_STRING = r"\".*\""

def t_IDENTIFIER(t):
    r"[a-zA-Z]([A-Za-z0-9])*"
    t.type = reserved.get(t.value,'IDENTIFIER')
    return t  

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore_COMMENT = r'\#.*'

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


