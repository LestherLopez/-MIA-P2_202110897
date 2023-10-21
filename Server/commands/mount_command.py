import os
import struct
from classes.Disk_Classes import *
from utils.Utils import *
from classes.State import estado
def mount_command(path_option, name_option, mount_list):
    print("----------------------------------------------------------")
    print("Comando MOUNT en ejecucion con los siguientes parametros:")
    print(f"Path: {path_option}")
    print(f"Name: {name_option}")
    id = "97"
    ruta_expandida = getPath(path_option)
    nombre_archivo_sin_extension = os.path.splitext(os.path.basename(str(ruta_expandida)))[0]
    if os.path.isfile(ruta_expandida):
        size_bytes =  os.path.getsize(str(ruta_expandida))
        with open(str(ruta_expandida), "rb") as file:
             # Desempaquetar los datos
            mbr_infosize =  file.read(struct.calcsize('I Q I c c c c  I I 16s c c c  I I 16s c c c  I I 16s c c c  I I 16s'))
            mbr_unpacked = struct.unpack("I Q I c c c c  I I 16s c c c  I I 16s c c c  I I 16s c c c  I I 16s", mbr_infosize)
           
            # Obtener los valores desempaquetados
            mbr_tamano = mbr_unpacked[0]
            mbr_fecha_creacion = mbr_unpacked[1]
            mbr_dsk_signature = mbr_unpacked[2]
            dsk_fit = mbr_unpacked[3].decode('utf-8')
            
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
            for i in range(0,4):
                str16 =  getString16(str(partitions[i].part_name))
                
                if str(str16) == name_option:
                    
                    id += str(i+1)
                   
                    id += str(nombre_archivo_sin_extension)
                    #verificar que el id no exista
                    
                    existe = any(d["id"] == id for d in mount_list)
                    if not existe:
                        mount_list.append({"id": id, "path": ruta_expandida, "size": partitions[i].part_s, "start": partitions[i].part_start})
                        print("Particion montada con exito")
                        estado.mensaje = "¡Particion montada con exito!"
                        print("----------------------------------------------------------")
                        return
                    else:
                        print("ERROR: No es posible montar la particion, puesto que ya esta montada")
                        estado.mensaje = "ERROR: No es posible montar la particion, puesto que ya esta montada"
                        print("----------------------------------------------------------")
                    #Nos ubicamos en particion con el nombre equivalente
                    
                        return
                elif( partitions[i].part_type=='E'): 
                    init = partitions[i].part_start
                    condicion = True
                    no_particion = 4
                    
                    while condicion:
                        file.seek(init)
                        ebr_infosize = file.read(struct.calcsize('c c I I i 16s'))
                        ebr_unpacked = struct.unpack('c c I I i 16s', ebr_infosize)
                        ebr_status =  ebr_unpacked[0].decode('utf-8')
                        ebr_fit = ebr_unpacked[1].decode('utf-8')
                        ebr_start = ebr_unpacked[2]
                        ebr_s = ebr_unpacked[3]
                        ebr_next = ebr_unpacked[4]
                        ebr_name = ebr_unpacked[5].decode('utf-8')
                        no_particion += 1
                        partitionlogic = EBR(ebr_status, ebr_fit, ebr_start, ebr_s, ebr_next, ebr_name)
                        str16 =  getString16(str(ebr_name))
                        if(str16 ==  str(name_option)):
                          
                            id += str(no_particion)
                            id += str(nombre_archivo_sin_extension)
                            #verificar que el id no exista
                            existe = any(d["id"] == id for d in mount_list)
                            if not existe:
                                mount_list.append({"id": id, "path": ruta_expandida, "size": partitions[i].part_s, "start": partitions[i].part_start})
                                print("Particion montada con exito")
                                estado.mensaje = "¡Particion montada con exito!"
                                print("----------------------------------------------------------")
                                
                            else:
                                print("ERROR: No es posible montar la particion, puesto que ya esta montada")
                                estado.mensaje = "ERROR: No es posible montar la particion, puesto que ya esta montada"
                                print("----------------------------------------------------------")
                            #Nos ubicamos en particion con el nombre equivalente
                            
                                
                            condicion = False
                            print("Particion montada con exito")
                            estado.mensaje = "¡Particion montada con exito!"
                            return
                        else:
                            init = ebr_next
                            condicion = True
                        if(ebr_next=="-1"):
                            print("La particion {} no exite".format(name_option))
                            estado.mensaje = "ERROR: La particion {} no exite".format(name_option)
                            return
    else:
        print("El path ingresado no existe")
        estado.mensaje = "ERROR: El path ingresado no existe"
    


def showMount(lista):
    print("-----------------------------")
    print("-----PARTICIONES MONTADA-----")
    stringres = "-----PARTICIONES MONTADA-----\n"
    for i in lista:
      stringres += i["id"]
      stringres += "\n"
      print(i["id"])
    stringres += "-----------------------------"
    print("-----------------------------")