import os
from utils.Utils import *
from classes.State import estado
def rmdisk_command(path_option):
    ruta_expandida = getPath(path_option)
    verifypath(str(ruta_expandida))
    print("---------------------------------------")
    print("Comando RMDISK en ejecucion con los siguientes parametros:")
    print(f"Path: {path_option}")   

    # If file exists, delete it.
    if os.path.isfile(str(ruta_expandida)):
        confirmacion = input("¿Estás seguro de que deseas eliminar el archivo dsk? (S/N): ").strip().lower()
        if confirmacion == "s":
            os.remove(str(ruta_expandida))
            print("Archivo eliminado con exito")
            estado.mensaje = "¡Archivo eliminado con exito!"
            print("---------------------------------------")
        else:
            print("Eliminacion cancelada")
            estado.mensaje = "¡Eliminacion cancelada!"
    else:
        # If it fails, inform the user.
        print("ERROR: %s archivo no encontrado" %ruta_expandida)
        estado.mensaje = "ERROR: %s archivo no encontrado" %ruta_expandida
        print("---------------------------------------")


#rmdisk -path="/home/user/mis discos/Disco3.dsk"