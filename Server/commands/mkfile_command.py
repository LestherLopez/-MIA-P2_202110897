import struct
from classes.Superblock import *
from classes.Block import *
from utils.Utils import *
from classes.InodeTable import *
def mkfile_command(path, r, size, cont, user_logueado, list_partitions):
    #verificar que el user logueado sea el root
    print("--------------------------------------------------")
    print("Comando MKFILE en ejecucion...")
    print(f"Path: {path}")
    print(f"Size: {size}")
    print(f"Cont: {cont}")
