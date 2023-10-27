import ply.yacc as yacc
# Obtener los tokens del lexer
from lexer_commands import *
from commands.mkdisk_command import mkdisk_command
from commands.fdisk_command import fdisk_command
from commands.rmdisk_command import rmdisk_command
from commands.mount_command import *
from utils.Utils import *
from commands.rep_command import rep_command
from commands.mkfs_command import *
from commands.login_command import *
from commands.unlogin_command import *
from commands.mkgrp_command import *
from commands.mkfile_command import *
from commands.mkdir_command import *
from classes.State import estado
list_mount_partitions = []
list_users = []
precedence = ()
sesion_activa = False
usuario_logueado = []

def p_init(t):
    'init : list_commands'
    t[0] = t[1]


# gramatica
def p_list_commands(t):
    '''list_commands : list_commands commands
                    | commands'''
    if len(t) != 2:
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]
    
def p_commands(t):
    '''commands : command_mkdisk
                | command_rmdisk
                | command_fdisk         
                | command_mount
                
                | command_mkfs
        
                | command_rep
                | PartitionsMount
                | command_login 
                | command_logout
                | command_mkgrp
                | command_mkfile
                | command_mkdir
                '''
    t[0] = t[1]


#MOSTRAR PARTITIONS MONTADAS
def p_command_partitionsmount(t):
    '''PartitionsMount : PM'''
    showMount(list_mount_partitions)

#comandos para administracion de discos
size_option = None
unit_option = 'M'
fit_option = 'FF'
path_option = None
name_option = None


#ADMINISTRACION DE DISCOS
#---------------------COMANDO MKDISK--------------------- (1)
def p_command_mkdisk(t):
    '''command_mkdisk : MKDISK parameters_mkdisk'''
    # t[0] : t[1] t[2] t[3]
    
   # command_mkdisk_(t[1])
    global size_option, unit_option, fit_option, path_option
    if(size_option == None ):
        print("ERROR: El parametro size es obligatorio")
        estado.mensaje = "ERROR: El parametro size es obligatorio"
    elif(path_option==None):
        print("ERROR: El parametro path es obligatorio")
        estado.mensaje = "ERROR: El parametro path es obligatorio"
    else:
        path_option_wc = remove_comillas(path_option)
        mkdisk_command(size_option, path_option_wc, fit_option, unit_option)
    size_option = None
    unit_option = 'M'
    fit_option = 'FF'
    path_option = None
 
    
def p_parameters_mkdisk(t):
    '''parameters_mkdisk : parameter_mkdisk parameters_mkdisk
                        |'''

def p_parameter_mkdisk(t):
    '''parameter_mkdisk : GUION SIZE IGUAL ENTERO
                        | GUION PATH IGUAL ROUTE
                        | GUION FIT IGUAL fit_options
                        | GUION UNIT IGUAL unit_options
                        '''
    
    global size_option, unit_option, fit_option, path_option
    
    if t[2] == 'size':
    
        size_option = t[4]
    elif t[2] == 'path':
        path_option = t[4]
    elif t[2] == 'fit':
        fit_option = t[4]
    elif t[2] == 'unit':
        unit_option = t[4]


    

#---------------------COMANDO RMDISK--------------------- (2)
def p_command_rmdisk(t):
    # recomendacion dejar el espacio
    '''command_rmdisk : RMDISK GUION PATH IGUAL ROUTE '''
    path_option = t[5]
    path_option_rm = remove_comillas(path_option)
    rmdisk_command(path_option_rm)
    
#---------------------COMANDO FDISK--------------------- (3)
unit_optionfdisk = 'K'
type_optionfdisk = 'P'
fit_optionfdisk = 'WF'

def p_command_fdisk(t):
    '''command_fdisk : FDISK parameters_fdisk'''
    global size_option, unit_optionfdisk, fit_optionfdisk, path_option, type_optionfdisk, name_option
    if(path_option==None):
        print("ERROR: El parametro path es obligatorio")
        estado.mensaje = "ERROR: El parametro path es obligatorio"
    elif(name_option == None):
        print("ERROR: El parametro name es obligatorio")
        estado.mensaje = "ERROR: El parametro name es obligatorio"
    else:
        path_option_wc = remove_comillas(path_option)
        name_option_wc = remove_comillas(name_option)
        fdisk_command(size_option, path_option_wc, str(name_option_wc), unit_optionfdisk, type_optionfdisk, fit_optionfdisk)
    unit_optionfdisk = 'K'
    type_optionfdisk = 'P'
    fit_optionfdisk = 'WF'
 
    size_option = None
    path_option = None
    name_option = None
def p_parameters_fdisk(t):
    '''parameters_fdisk : parameter_fdisk parameters_fdisk
                        |'''
def p_parameter_fdisk(t):
    '''parameter_fdisk : GUION SIZE IGUAL ENTERO
                      | GUION PATH IGUAL ROUTE
                      | GUION NAME IGUAL ID
                      | GUION UNIT IGUAL unit_options
                      | GUION TYPE IGUAL type_options
                      | GUION FIT IGUAL fit_options'''
    global size_option, unit_optionfdisk, fit_optionfdisk, path_option, type_optionfdisk, name_option
    if t[2] == 'size':
        #print(t[4])
        size_option = t[4]
    elif t[2] == 'path':
        path_option = t[4]
    elif t[2] == 'name':
        name_option = t[4]
    elif t[2] == 'fit':
        fit_optionfdisk = t[4]
    elif t[2] == 'unit':
        unit_optionfdisk = t[4]
    elif t[2] == 'type':
        type_optionfdisk = t[4]


#---------------------COMANDO MOUNT--------------------- (4)
def p_command_mount(t):
    '''command_mount : MOUNT parameters_mount'''
    global name_option, path_option, list_mount_partitions
    if(name_option == None ):
        print("ERROR: El parametro name es obligatorio")
        estado.mensaje = "ERROR: El parametro name es obligatorio"
    elif(path_option==None):
        print("ERROR: El parametro path es obligatorio")
        estado.mensaje = "ERROR: El parametro path es obligatorio"
    else:
        path_option_moun = remove_comillas(path_option)
        name_option_moun = remove_comillas(name_option)
        mount_command(str(path_option_moun), str(name_option_moun), list_mount_partitions)
    
def p_parameters_mount(t):
    '''parameters_mount : parameter_mount parameters_mount
                        |'''

def p_parameter_mount(t):
    '''parameter_mount :  GUION PATH IGUAL ROUTE
                        | GUION NAME IGUAL ID
                        '''
    global name_option, path_option
    if t[2] == 'name':
      
        name_option = t[4]
    elif t[2] == 'path':
        path_option = t[4]




#ADMINISTRACION DE ARCHIVOS
#---------------------COMANDO MKFS--------------------- (5)
id_mkfs = None
type_mkfs = 'full'
fs_mkfs = '2fs'
def p_command_mkfs(t):
    '''command_mkfs : MKFS parameters_mkfs'''
    global id_mkfs, type_mkfs, fs_mkfs
    if(id_mkfs==None):
        print("ERROR: El parametro id es obligatorio para ejecutar el comando MKFS")
        estado.mensaje = "ERROR: El parametro id es obligatorio para ejecutar el comando MKFS"
    else:
        mkfs_command(id_mkfs, type_mkfs, fs_mkfs, list_mount_partitions, list_users)
    id_mkfs = None
    type_mkfs = 'full'
    fs_mkfs = '2fs'
def p_parameters_mkfs(t):
    '''parameters_mkfs : parameter_mkfs parameters_mkfs
                        |'''
    
def p_parameter_mkfs(t):
    '''parameter_mkfs : GUION IDDISK IGUAL ENTERO ID
                     | GUION TYPE IGUAL FULL
                     | GUION FS IGUAL ENTERO FS'''
    global id_mkfs, type_mkfs, fs_mkfs
    if t[2] == 'id':
        concatenado = str(t[4])+str(t[5])
        id_mkfs = remove_comillas(concatenado)
    elif t[2] == 'fs':
        concatenadofs = str(t[4])+str(t[5])
        fs_mkfs = remove_comillas(concatenadofs)
    elif t[2] == 'type':
        type_mkfs = t[4]




#ADMINISTRACION DE USUARIOS Y GRUPOS
#---------------------COMANDO LOGIN--------------------- (6)
user_login = None
pass_login = None
id_login = None
def p_command_login(t):
    '''command_login : LOGIN parameters_login'''
    global user_login, pass_login, id_login, sesion_activa, usuario_logueado
    if(user_login==None):
        print("ERROR: El parametro user es obligatorio para ejecutar el comando LOGIN")
        estado.mensaje = "El parametro user es obligatorio para ejecutar el comando LOGIN"
    elif(pass_login==None):
        print("ERROR: El parametro pass es obligatorio para ejecutar el comando LOGIN")
        estado.mensaje = "El parametro pass es obligatorio para ejecutar el comando LOGIN"
    elif(id_login==None):
        print("ERROR: El parametro id es obligatorio para ejecutar el comando LOGIN")
        estado.mensaje = "El parametro id es obligatorio para ejecutar el comando LOGIN"
    else:
       
        newsesion_activa = login_command(user_login, pass_login, id_login, list_mount_partitions,sesion_activa, list_users, usuario_logueado)

        sesion_activa = newsesion_activa

    
def p_parameters_login(t):
    '''parameters_login : parameter_login parameters_login
                        | '''
    
def p_parameter_login(t):
    '''parameter_login : GUION IDDISK IGUAL ENTERO ID
                        | GUION USER IGUAL ID
                        | GUION PASS IGUAL ENTERO
                        | GUION PASS IGUAL ID'''
    global user_login, pass_login, id_login
    if t[2] == 'id':
        concatenado = str(t[4])+str(t[5])
        id_login = remove_comillas(concatenado)
    elif t[2] == 'pass':
        concatenadopass = str(t[4])
        pass_login = remove_comillas(concatenadopass)
    elif t[2] == 'user':
        user_login = str(t[4])
#---------------------COMANDO LOGOUT--------------------- (7)
def p_command_logout(t):
    '''command_logout : LOGOUT'''
    global sesion_activa, usuario_logueado
    newsesions = unlogin_command(sesion_activa, usuario_logueado)
    sesion_activa = newsesions
#---------------------COMANDO MKGRP--------------------- (8)
def p_command_mkgrp(t):
    '''command_mkgrp : MKGRP GUION NAME IGUAL ID'''
    global usuario_logueado, list_mount_partitions
    name_mkgrp = str(t[5])
    namemkgrp = remove_comillas(name_mkgrp)
    mkgrp_command(namemkgrp, usuario_logueado, list_mount_partitions)
    name_mkgrp = None
#---------------------RMGRP--------------------- (9)

#---------------------MKUSR--------------------- (10)

#---------------------RMUSR--------------------- (11)




#ADMINISTRACION DE CARPETAS Y ARCHIVOS
#---------------------MKFILE--------------------- (12)
path_mkfile = None
size_mkfile = None
cont_mkfile = None
r_mkfile = None
def p_command_mkfile(t):
    '''command_mkfile : MKFILE parameters_mkfile'''
    global path_mkfile, size_mkfile, cont_mkfile, r_mkfile
    if(path_mkfile==None):
        print("ERROR: El parametro path es obligatorio para el comando mkfile")
        estado.mensaje = "El parametro path es obligatorio para el comando mkfile"
    else:
        path = remove_comillas(path_mkfile)
        mkfile_command(path, r_mkfile, size_mkfile, cont_mkfile, usuario_logueado, list_mount_partitions)
    path_mkfile = None
    size_mkfile = None
    cont_mkfile = None
    r_mkfile = None
def p_parameters_mkfile(t):
    '''parameters_mkfile : parameter_mkfile parameters_mkfile
                        |'''
def p_parameter_mkfile(t):
    '''parameter_mkfile : GUION PATH IGUAL ROUTE
                        | GUION SIZE IGUAL ENTERO
                        | GUION CONT IGUAL ROUTE
                        | GUION R'''
    global path_mkfile, size_mkfile, cont_mkfile, r_mkfile
    if t[2] == 'path':
        path_mkfile = t[4]
    elif t[2] == 'size':
        size_mkfile = t[4]
    elif t[2] == 'cont':
        cont_mkfile = t[4]
    elif t[2] == 'r':
        r_mkfile = t[2]
#---------------------MKDIR--------------------- (13)
path_mkdir = None
r_mkdir = None
def p_command_mkdir(t):
    '''command_mkdir : MKDIR parameters_mkdir'''
    global path_mkdir, r_mkdir
    if(path_mkdir==None):
        print("ERROR: El parametro path es obligatorio para el comando mkdir")
        estado.mensaje = "El parametro path es obligatorio para el comando mkdir"
    else:
        path = remove_comillas(path_mkdir) 
        mkdir_command(path, r_mkdir, usuario_logueado, list_mount_partitions)
    path_mkdir = None
    r_mkdir = None
def p_parameters_mkdir(t):
    '''parameters_mkdir : parameter_mkdir parameters_mkdir
                        |'''
def p_parameter_mkdir(t):
    '''parameter_mkdir : GUION PATH IGUAL ROUTE
                        | GUION R'''
    global path_mkdir, r_mkdir
    if t[2] ==  'path':
        path_mkdir = t[4]
    elif t[2] == 'r':
        r_mkdir = t[2]
#---------------------PAUSE--------------------- (14)




#---------------------REP--------------------- (15)
ruta_option = None
id_option = None
def p_command_rep(t):
    '''command_rep : REP parameters_rep'''
    global ruta_option, name_option, id_option, path_option
    if(id_option == None ):
        print("ERROR: El parametro id es obligatorio")
        estado.mensaje = "El parametro id es obligatorio"
    elif(path_option==None):
        print("ERROR: El parametro path es obligatorio")
        estado.mensaje = "El parametro path es obligatorio"
    elif(name_option == None):
        print("ERROR: El parametro name es obligatorio")
        estado.mensaje = "El parametro name es obligatorio"
        
    else:
        path_option_wc = remove_comillas(path_option)
        name_option_wc = remove_comillas(name_option)
        id_option_wc = remove_comillas(id_option)
    
        rep_command(str(path_option_wc), str(name_option_wc), str(id_option_wc), ruta_option, list_mount_partitions)
        
def p_parameters_rep(t):
    '''parameters_rep : parameter_rep parameters_rep
                       | '''
    
def p_parameter_rep(t):
    '''parameter_rep  :  GUION PATH IGUAL ROUTE
                        | GUION IDDISK IGUAL ENTERO ID
                        | GUION NAME IGUAL ID
                        | GUION RUTA IGUAL ROUTE '''
    global name_option, id_option, path_option, ruta_option
    if t[2] == 'name':
        name_option = t[4]
    elif t[2] == 'path':
        path_option = t[4]
    elif t[2] == 'id':
        id_option  = (str(t[4])+str(t[5]))
    elif t[2] == 'ruta':
        ruta_option = t[4]


#TIPOS
def p_fit_options(t):
    '''fit_options : FIRSTFIT
                    | BESTFIT
                    | WORSTFIT'''
    t[0] = t[1]
def p_unit_options(t):
    '''unit_options : KILOBYTE
                    | MEGABYTE
                    | BYTES'''
    t[0] = t[1]

def p_type_options(t):
    '''type_options : PRIMARY 
                    | EXTENDED
                    | LOGIC'''
    t[0] = t[1]

def p_error(t):

    print("ERROR: El siguiente comando o parametro no existe '%s'" % t.value)
    estado.mensaje = "ERROR: El siguiente comando o parametro no existe '%s'" % t.value
def remove_comillas(cadena):
    if cadena.startswith('"') and cadena.endswith('"'):
        return cadena[1:-1]  
    return cadena

# llevarla al main
def parse(input):
    global errors
    global parser
    parser = yacc.yacc()
    lexer.lineno = 1
    parser.parse(input)
    return
