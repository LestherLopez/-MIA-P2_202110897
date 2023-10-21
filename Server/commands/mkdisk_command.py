import os
from datetime import *
import random
from classes.Disk_Classes import *
from utils.Utils import *
from classes.State import estado
def mkdisk_command(size_option, path_option, fit_option, unit_option):
    print("---------------------------------------")
    print("Comando MKDISK en ejecucion con los siguientes parametros:")
    print(f"Size: {size_option}")
    print(f"Unit: {unit_option}")
    print(f"Fit: {fit_option}")
    print(f"Path: {path_option}")
    if(int(size_option)>0):
        ruta_expandida = getPath(path_option)
        verifypath(str(ruta_expandida))
        
        with open(str(ruta_expandida), "wb") as file:
            num_zeros = getnum_zeros(size_option, unit_option)     
            
            file.write(b'\x00' * num_zeros)
            fit_mbr = getfit_mbr(str(fit_option))
            #obtener fecha
            fecha_actual = datetime.now()
            fecha_int = int(fecha_actual.strftime("%d%m%Y%H%M"))
           
            # CREACION DE LAS CAUTRO PARTICIONES
            partition1 = Partition("0", "0", "0", 0, 0, "0000000000000000")
            partition2 =  Partition("0", "0", "0", 0, 0, "0000000000000000")
            partition3 = Partition("0", "0", "0", 0, 0, "0000000000000000")
            partition4 = Partition("0", "0", "0", 0, 0, "0000000000000000")
            mbr_data = MBR(num_zeros, fecha_int, random.randint(0,100), fit_mbr, partition1, partition2, partition3, partition4)
            #empaquetar MBR y partitions
            mbr_datapack = mbr_data.pack()
            file.seek(0)          
            file.write(mbr_datapack)
            print("Disco creado con exito")
            estado.mensaje = "¡Disco creado con exito!"
            print("---------------------------------------")
    elif(int(size_option)<=0):
        print("ERROR: El parametro size tiene que ser mayor a 0")
        estado.mensaje = "ERROR: El parametro size tiene que ser mayor a 0"
        print("---------------------------------------")
def getnum_zeros(size, unit):
    if(str(unit)=="M"):
        return (int(size)*1024*1024)
    elif(str(unit)=="K"):
        return (int(size)*1024)
    elif(str(unit)=="B"):
        return int(size)
    else:
        print("La unidad de medida es incorrecta")
        estado.mensaje = "ERROR: La unidad de medida es incorrecta"


def getfit_mbr(fitop):
    if(fitop=="FF"):
        return "F"
    elif(fitop=="BF"):
        return "B"
    elif(fitop=="WF"):
        return "W"
    else:
        print("ERROR: Fit incorrecto")
        estado.mensaje = "ERROR: La unidad de medida es incorrecta"
