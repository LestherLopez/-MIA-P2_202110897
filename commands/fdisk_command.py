import os
import struct
from classes.Disk_Classes import *
from utils.Utils import *
def fdisk_command(size_option, path_option_wc, name_option_wc, unit_optionfdisk, type_optionfdisk, fit_optionfdisk, deleteoption):
    #verificar existencia de fdisk
    print("---------------------------------------")
    print("Comando FDISK en ejecucion con los siguientes parametros:")
    print(f"Size: {size_option}")
    print(f"Unit: {unit_optionfdisk}")
    print(f"Fit: {fit_optionfdisk}")
    print(f"Path: {path_option_wc}")
    print(f"Type: {type_optionfdisk}")
    print(f"Name: {name_option_wc}")
    print(f"Delete: {deleteoption}")
    ruta_expandida = getPath(path_option_wc)
   
    if os.path.isfile(str(ruta_expandida)):
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
            partitions = getPartitions(mbr_unpacked)
            
            #verificar si es eliminar si no entonces continuar al agregado de particiones
            if str(deleteoption)=="full":
                #eliminar particion
                #recorrer particiones
                for i in range(0,4):
                    name = getString16(partitions[i].part_name)
                    if(partitions[i].part_type=='P'):
                        if name==str(name_option_wc):
                            partitions[i].part_status = "0"
                            partitions[i].part_type = "0"
                            partitions[i].part_fit ="0"
                            partitions[i].part_start = 0
                            partitions[i].part_s = 0
                            partitions[i].part_name = "0000000000000000"
                            print("¡Particion Primaria eliminada con exito!")
                            break
                    elif(partitions[i].part_type=='E'):
              
                        if name==str(name_option_wc):
                            partitions[i].part_status = "0"
                            partitions[i].part_type = "0"
                            partitions[i].part_fit ="0"
                            partitions[i].part_start = 0
                            partitions[i].part_s = 0
                            partitions[i].part_name = "0000000000000000"
                            print("¡Particion Extendida eliminada con exito!")
                            break
            
                        #revisar en las logicas de la extendida    
                        else:
                        
                            condicion = True
                            init = partitions[i].part_start
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
                                name = getString16(ebr_name)
                           
                                if (name==str(name_option_wc)):
                             
                                    with open(str(ruta_expandida), "rb+") as filea:
                                        #sumar al next del logic anterior el size del ebr a borrar
                                        
                                        filea.seek(partitions[i].part_start)
                                        
                                        ebr_infosizea = filea.read(struct.calcsize('c c I I i 16s'))
                                     
                                        ebr_unpackeda = struct.unpack('c c I I i 16s', ebr_infosizea)
                                     
                                        ebr_statusa =  ebr_unpackeda[0].decode('utf-8')
                                     
                                        ebr_fita = ebr_unpackeda[1].decode('utf-8')
                                     
                                        ebr_starta = ebr_unpackeda[2]
                                   
                                        ebr_sa = ebr_unpackeda[3]
                                      
                                        ebr_nexta = ebr_unpackeda[4]
                                      
                                        ebr_namea = ebr_unpackeda[5].decode('utf-8')

                                       
                                        current_ebr = EBR("1", ebr_fita, ebr_starta, ebr_sa, ebr_nexta+ebr_s, ebr_namea)
                                        current_ebrpack = current_ebr.pack()
                                       
                                        filea.write(current_ebrpack)
                                       


                                        #borrar
                                        filea.seek(init)
                                      
                                        filea.write(b'\x00' * int(struct.calcsize('c c I I i 16s')))
                                        print("¡Particion Logica eliminada con exito!")
                                    condicion = False  
                                else: 
                                    #actualizar el init por el ebr_next
                                    init = ebr_next
                            return
            # su no es eliminar entonces es crear normal
            else:
                
                #verificar si ya hay 4 partitions
                if str(type_optionfdisk)!="L":
                    contador = 0
                    for i in range(0,4):
                        if partitions[i].part_name == "0000000000000000":
                            continue
                        else:
                            contador +=1 
                    if contador == 4:
                        print("ERROR: El disco ya contiene 4 particions")
                        return
                    
        #       if(dsk_fit=="F"):
                
                if(str(type_optionfdisk)=="P" ):
                    
                    
                    for i in range(0,4):
                        #verificar el primer vacio 
                        if partitions[i].part_name == "0000000000000000" and partitions[i].part_status == "0":
                            #prmario y first fit
                        
                            #EBR VA CON VALORES NULOS MENOS NEXT ESE VA CON -1
                        

                            sizepart_bytes = getSize_bytes(size_option, unit_optionfdisk)
                            fitOP = getfit_mbr(str(fit_optionfdisk))
                            start_number = getStartpart(partitions[i-1].part_start, partitions[i-1].part_s)
                            partitions[i].part_status = "1"
                            partitions[i].part_type = type_optionfdisk
                            partitions[i].part_fit =fitOP
                            partitions[i].part_start = start_number
                            partitions[i].part_s = sizepart_bytes
                            partitions[i].part_name = str(name_option_wc)
                            #crear ebr si es extendida

                            break
                elif(str(type_optionfdisk)=="E"):      
                    value = verificar_extendidas(partitions)
                    if value:
                        for i in range(0,4):
                            #verificar el primer vacio 
                            if partitions[i].part_name == "0000000000000000" and partitions[i].part_status == "0":
                                #prmario y first fit
                            
                                #EBR VA CON VALORES NULOS MENOS NEXT ESE VA CON -1
                            

                                sizepart_bytes = getSize_bytes(size_option, unit_optionfdisk)
                                fitOP = getfit_mbr(str(fit_optionfdisk))
                                start_number = getStartpart(partitions[i-1].part_start, sizepart_bytes)
                                partitions[i].part_status = "1"
                                partitions[i].part_type = type_optionfdisk
                                partitions[i].part_fit =fitOP
                                partitions[i].part_start = start_number
                                partitions[i].part_s = sizepart_bytes
                                partitions[i].part_name = str(name_option_wc)
                                #crear ebr si es extendida

                                break
                    else:
                        print("ERROR: El disco no puede contener mas de una particion extendida")
                        print("---------------------------------------")
                        return
                elif(str(type_optionfdisk)=="L"):
                
                    sizepart_bytes = getSize_bytes(size_option, unit_optionfdisk)
                    existeExtendida =  False
                    fitOP = getfit_mbr(str(fit_optionfdisk))
                    for i in range(0,4):
                        
                        if(partitions[i].part_type=='E'):
                            existeExtendida = True
                    
                            break
                            
                    if existeExtendida:
                        
                            createLogic(partitions, str(ruta_expandida), fitOP, sizepart_bytes, str(name_option_wc))
                    else:
                            print("ERROR: No es posible crear una particion logica sin particiones extendidas");
                            print("---------------------------------------")
                            return
                    return

                    
            """"   
            elif(dsk_fit=="W"):
                print("Worst fit")
            elif(dsk_fit=="B"):
                print("Best fit")
            """
            mbr_obj = MBR(mbr_tamano, mbr_fecha_creacion, mbr_dsk_signature, dsk_fit, partitions[0], partitions[1], partitions[2], partitions[3])
            new_mbr_data = struct.pack(
            "I Q I c c c c  I I 16s c c c  I I 16s c c c  I I 16s c c c  I I 16s",
            mbr_obj.mbr_tamano, mbr_fecha_creacion, mbr_obj.mbr_dsk_signature,
            mbr_obj.dsk_fit.encode('utf-8'),
            partitions[0].part_status.encode('utf-8'),
            partitions[0].part_type.encode('utf-8'),
            partitions[0].part_fit.encode('utf-8'),
            partitions[0].part_start,
            partitions[0].part_s,
            partitions[0].part_name.encode('utf-8'),
            partitions[1].part_status.encode('utf-8'),
            partitions[1].part_type.encode('utf-8'),
            partitions[1].part_fit.encode('utf-8'),
            partitions[1].part_start,
            partitions[1].part_s,
            partitions[1].part_name.encode('utf-8'),
            partitions[2].part_status.encode('utf-8'),
            partitions[2].part_type.encode('utf-8'),
            partitions[2].part_fit.encode('utf-8'),
            partitions[2].part_start,
            partitions[2].part_s,
            partitions[2].part_name.encode('utf-8'),
            partitions[3].part_status.encode('utf-8'),
            partitions[3].part_type.encode('utf-8'),
            partitions[3].part_fit.encode('utf-8'),
            partitions[3].part_start,
            partitions[3].part_s,
            partitions[3].part_name.encode('utf-8')
            )
            
     
            file.close()
        with open(str(ruta_expandida), "wb") as file:
            file.write(b'\x00' * size_bytes)
            file.seek(0)
            file.write(new_mbr_data)
            file.close()
       
       #CREAR EBR SI ES EXTENDIDA
        for i in range(0,4):
            if(partitions[i].part_type=='E'):
                createEBR(ruta_expandida, partitions[i].part_start)
                
                break
            
    else:
        print("ERROR: el path del archivo ingresado no existe o el archivo no existe con extension dsk")
        print("---------------------------------------")
    


#contiene el tamaño total de la partición en bytes.
def getSize_bytes(number, unit):
    if unit == "B":
        return number
    elif unit == "K":
        return (number*1024)
    elif unit == "M":
        return (number*1000000)
    
def getfit_mbr(fitop):
    if(fitop=="FF"):
        return "F"
    elif(fitop=="BF"):
        return "B"
    elif(fitop=="WF"):
        return "W"
    else:
        print("ERROR: Fit incorrecto")


def createEBR(path, init):
   
    with open(str(path), "rb+") as file:
       
        new_ebr = EBR("0", "0", 0, 0, -1, "0000000000000000")
        ebr_pack = new_ebr.pack()
        file.seek(init)
        file.write(ebr_pack)
        file.close()



def createLogic(partitions, path, fit, size, name):
    for i in range(0,4):
       
        if(partitions[i].part_type=='E'):
           
            with open(str(path), "rb+") as file: 
                init = partitions[i].part_start
                condicion = True
                while condicion:
                    #ubicarse en donde inicia el ebr
                    file.seek(init)
                    ebr_infosize = file.read(struct.calcsize('c c I I i 16s'))
                    ebr_unpacked = struct.unpack('c c I I i 16s', ebr_infosize)
                    ebr_status =  ebr_unpacked[0].decode('utf-8')
                    ebr_fit = ebr_unpacked[1].decode('utf-8')
                    ebr_start = ebr_unpacked[2]
                    ebr_s = ebr_unpacked[3]
                    ebr_next = ebr_unpacked[4]
                    ebr_name = ebr_unpacked[5].decode('utf-8')
                    #si ebr_next es -1 escribir la logica  
                    if (int(ebr_next)==-1):
                        #si es el ebr inicial que trae la extendida escribir aqui la logica
                        if(int(ebr_start)!=int(init)):
                            #actualizar primer ebr
                            ebr_status="1"
                            ebr_fit = fit
                            ebr_start = init
                            ebr_s = size
                            ebr_next = -1
                            ebr_name = name
                            ebr_update = EBR(ebr_status, ebr_fit, ebr_start, ebr_s, ebr_next, ebr_name)
                            ebr_updatepack = ebr_update.pack()
                            file.seek(init)
                            file.write(ebr_updatepack)
                            file.close()          
                        #si no escribir en otro posicion que no sea el primer ebr que trae la particion             
                        else:
                            current_ebr = EBR("1", ebr_fit, ebr_start, ebr_s, (init+ebr_s), ebr_name)
                            current_ebrpack = current_ebr.pack()
                            file.seek(init)
                            file.write(current_ebrpack)
                            #write new logic
                            ebr_status="1"
                            ebr_fit = fit
                            ebr_start = init+ebr_s
                            ebr_s = size
                            ebr_next = -1
                            ebr_name = name
                            new_ebr = EBR("1", ebr_fit, ebr_start, ebr_s, ebr_next, ebr_name)
                            ebr_pack = new_ebr.pack()
                            file.seek(int(ebr_start))
                            file.write(ebr_pack)
                            file.close()
                        condicion = False
                    else: 
                        #actualizar el init por el ebr_next
                        init = ebr_next

                        

            return
        
    print("ERROR: no se encuentran particiones extendidas para ingresar una particion logica")
def verificar_extendidas(partitions):
    contador = 0
    for i in range(0,4):
        if partitions[i].part_type=='E':
            contador += 1
        
    if contador==0:
        return True
    else:
        return False
#execute -path="/home/user/prueba.eea"
