import ply.yacc as yacc

from Lexer import tokens

precedence = (
    ('left', '|', '&'),
    ('left', '<', '>', '='),
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS'),
)

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




