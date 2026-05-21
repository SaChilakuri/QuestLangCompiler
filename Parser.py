import ply.yacc as yacc

from Lexer import tokens

precedence = (
    ('left', '|', '&'),
    ('left', '<', '>', '='),
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS'),
)

# Simple prompt format, returns a tuple with None as first element
def p_prompt_simple(p):
    '''prompt : PROMPT ':' expression ';' '''
    p[0] = (None, input(p[3][1:-1] + " "))

# Complex prompt format, returns a tuple with the variable as first element
def p_prompt_complex(p):
    '''prompt : PROMPT '[' IDENTIFIER ']' ':' expression ';' '''
    p[0] = (p[3], input(p[6][1:-1] + " "))

def p_expressions(p):
    '''expression : term'''
    p[0] = p[1]

def p_expression_recursive(p):
    '''expression : term '+' term

                  | term '-' term
                  | term '*' term
                  | term '/' term

                  | term '&' term
                  | term '|' term
                  | term '<' term

                  | term '>' term
                  | term '=' term'''
    if p[2] == '+':    p[0] = p[1] + p[3]
    elif p[2] == '-':  p[0] = p[1] - p[3]
    elif p[2] == '*':  p[0] = p[1] * p[3]
    elif p[2] == '/':  p[0] = p[1] / p[3]
    elif p[2] == '&':  p[0] = p[1] and p[3]
    elif p[2] == '|':  p[0] = p[1] or p[3]
    elif p[2] == '<':  p[0] = p[1] < p[3]
    elif p[2] == '>':  p[0] = p[1] > p[3]
    elif p[2] == '=':  p[0] = p[1] == p[3]

def p_term_unaryOp(p):
    '''term : '-' term %prec UMINUS
            | '~' term'''
    if p[1] == '-':
        p[0] = -p[2]
    elif p[1] == '~':
        p[0] = not p[2]

def p_term_constants(p):
    '''term : INTEGER
            | STRING
            | IDENTIFIER'''
    p[0] = p[1]

# Build the parser and write a test line
parser = yacc.yacc()
result = parser.parse('prompt[a] : "What is your strength?" ;')
print(result)




