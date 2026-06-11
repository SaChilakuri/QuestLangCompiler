import ply.yacc as yacc
import SymbolTable as table

from Lexer import tokens

global_table=table.SymbolTable()
current_table=global_table()

precedence = (
    ('left', '|', '&'),
    ('left', '<', '>', '?'),
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS'),
)

# #Handles blueprints (sets the scope to the global one after completion)
# def p_blueprint(p):
#     '''blueprint_decl: blueprint_header blueprint_variable_declarations subroutine_declarations '}' '''
#     current_table=global_table

# #Seperate rule created to handle creating the symbol_table before the variables are declared
# def p_blueprint_header(p):
#     '''blueprint_header: BLUEPRINT IDENTIFIER '{' '''
#     blueprint_name = p[2]
#     current_table = table.SymbolTable(global_table)
#     symbol = table.Symbol(blueprint_name,'class',current_table)
#     global_table.insert(symbol)

# #handles empty stuff (and provides base cases)
# def p_empty(p):
#     '''empty: '''

# #handles blueprint variables
# def p_blueprint_variables(p):
#     '''blueprint_variable_declarations : blueprint_variable_declarations blueprint_variable_decl
#                                        | empty'''
    
#     if len(p) == 3:
#         p[0]=p[1]+[p[2]]
#     else:
#         p[0]=[]

# #handles subroutine declarations
# def p_subroutine_declarations(p):
#     '''subroutine_declarations: subroutine_declarations subroutine_declaration
#                               |'''
    
#     if len(p) == 3:
#         p[0]=p[1]+[p[2]]
#     else:
#         p[0]=[]


    

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
                  | term '?' term'''
    if p[2] == '+':    p[0] = p[1] + p[3]
    elif p[2] == '-':  p[0] = p[1] - p[3]
    elif p[2] == '*':  p[0] = p[1] * p[3]
    elif p[2] == '/':  p[0] = p[1] / p[3]
    elif p[2] == '&':  p[0] = p[1] and p[3]
    elif p[2] == '|':  p[0] = p[1] or p[3]
    elif p[2] == '<':  p[0] = p[1] < p[3]
    elif p[2] == '>':  p[0] = p[1] > p[3]
    elif p[2] == '?':  p[0] = p[1] == p[3] 

def p_term_unaryOp(p):
    '''term : '-' term %prec UMINUS
            | '~' term'''
    if p[1] == '-':
        p[0] = -p[2]
    elif p[1] == '~':
        p[0] = not p[2]

def p_term_constants(p):
    '''term : INTEGER
            | STRING'''
    p[0] = p[1]

# Build the parser and write a test line
parser = yacc.yacc()
result = parser.parse('prompt[a] : "What is your strength?" ;')
print(result)




