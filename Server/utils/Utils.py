import os
from classes.Disk_Classes import *
import re
#function to get the path without user string 
def getPath(path):
    #obtener usuario
    username = os.getenv('USER')
    # Sustituir "user" con el nombre de usuario actual en la ruta
    corrected_path = path.replace("user", "lesther")
    return corrected_path

#function to create folders if they are not existing
def verifypath(path):
    directorio = os.path.dirname(path)
    if not os.path.exists(directorio):
        os.makedirs(directorio)


#function to get the start of partitions
def getStartpart(start_previous, size_current):
    
    if start_previous==0:
       
        return int(132)
    else:
        start = int(start_previous) + int(size_current)
        return int(start)


def getNExtEBR():
    return -1


def getPartitions(mbr_unpacked):
    partitions = []
    for i in range(4, len(mbr_unpacked), 6):

        part_status = mbr_unpacked[i].decode('utf-8')
        part_type = mbr_unpacked[i + 1].decode('utf-8')
        part_fit = mbr_unpacked[i + 2].decode('utf-8')
        part_start = mbr_unpacked[i + 3]
        part_s = mbr_unpacked[i + 4]
        part_name = mbr_unpacked[i + 5].decode('utf-8')
        partition = Partition(part_status, part_type, part_fit, part_start, part_s, part_name)
        partitions.append(partition)
    return partitions

def getString16(cadena):
    cadena_limpia = cadena.rstrip()  # Elimina los espacios en blanco al final
    resultado = ''.join(filter(str.isalnum, cadena_limpia))
    return resultado

def getStringWithDot(cadena):
    caracteres_permitidos = re.compile(r'[^a-zA-Z0-9\n,.;:?!\'"\t ]')
    resultado = caracteres_permitidos.sub('', cadena)
    return resultado


def getPercentOcupation(size_toCalculate, sizedsk):
    percent = (size_toCalculate/sizedsk)*100
    percent = round(percent, 3)

    return percent

def getFreeSpace(inicio, final):
    return (final-inicio)