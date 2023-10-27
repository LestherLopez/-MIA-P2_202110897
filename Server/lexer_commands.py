

import ply.lex as lex
# Lista de errores
errors = []

# palabras reservadas
reserved_words = {
    # Manage disk
    # MKDISK -> mkdisk >size=3000 >unit=K >path=”/home/user/Disco1.dsk”
    # cadena a reconocer : nombre var  


    #comandos de administracion de discos
    'mkdisk' : 'MKDISK', 
    'rmdisk' : 'RMDISK',
    'fdisk'  : 'FDISK',
    'mount'  : 'MOUNT',
    'unmount': 'UNMOUNT',
    'mkfs'   : 'MKFS',
    'rep' : 'REP',
    'execute' : 'EXECUTE',
    #parameters
    'size': 'SIZE',
    'unit': 'UNIT',
    'path': 'PATH',
   
    'fit': 'FIT',
    'name': 'NAME',
    'type': 'TYPE',
    'delete': 'DELETE',
    'add': 'ADD',
    'id': 'IDDISK',
    'fs':  'FS',
    'K': 'KILOBYTE',
    'BF': 'BESTFIT',
    'FF': 'FIRSTFIT',
    'WF': 'WORSTFIT',
    'M': 'MEGABYTE',
    'B': 'BYTES',
    'P': 'PRIMARY',
    'E': 'EXTENDED',
    'L': 'LOGIC',
    'full': 'FULL',
    'ruta': 'RUTA',
    'mkfs':  'MKFS',
    'showmount': 'PM',
    'Login':    'LOGIN',
    'logout':    'LOGOUT',
    'user':         'USER',
    'pass': 'PASS',
    'mkgrp': 'MKGRP',
    "mkfile": 'MKFILE',
    "mkdir":  'MKDIR',
    "cont": 'CONT',
    "r":    'R',

    #Valores
}

# Lista de tokens GLOBAL tokens es una palabra del analizador
tokens = [
    'ENTERO',
    'ID',
   'CADENA',   
   'IGUAL',
   'MAYOR_QUE',
   'ROUTE',
   'GUION'
] + list(reserved_words.values())


# Expresiones regulares para tokens simples
t_IGUAL = r'\=' 
t_MAYOR_QUE = r'\>'
t_GUION = r'\-'
# Expresiones regulares con acciones de codigo 55 
# todo ingresa como un string  "55" int(55) 
#  ID mkdir -> ID mkdisk

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'(\"[a-zA-Z_][a-zA-Z_0-9]*\")|(\'[a-zA-Z_][a-zA-Z_0-9]*\')|([a-zA-Z_][a-zA-Z_0-9]*)|([0-9][a-zA-Z_0-9]*)'

    t.type = reserved_words.get(t.value, 'ID') 
    return t



#  Path (falta validar bien las comillas)
def t_ROUTE(t):
    r'(\/[^\s]+)|(\"[^\"]*\")|(\'[^\']*\')'
    return t
# Ignorar comentarios (empiezan con # y terminan en nueva línea)
def t_COMMENT(t):
    r'\#.*'
    return None
#  Cadena 
def t_CADENA(t):
    r'\"(.|\n)*?\"'
    t.value = t.value[1:-1] # remuevo las comillas
    return t


# New line
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#  Caracteres ignorados
t_ignore = ' \t'

def t_error(t):
    errors.append(t.value[0])
    print(f'Comando no reconocido: {t.value[0]} en la linea {t.lexer.lineno}')
    t.lexer.skip(1)

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

lexer = lex.lex()

