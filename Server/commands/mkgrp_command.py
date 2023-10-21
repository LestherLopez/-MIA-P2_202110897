import struct
from classes.Superblock import *
from classes.Block import *
from utils.Utils import *
from classes.InodeTable import *
def mkgrp_command(name, user_logueado, list_partitions):
    #verificar que el user logueado sea el root
    print("Comando MKGRP en ejecucion...")
    print(f"Name: {name}")
    search_inodo = -1
    if(len(user_logueado)==1):
        
        if str(user_logueado[0]["user"]) == "root" and str(user_logueado[0]["password"])=="123":
            
            for partition in list_partitions:
                if partition["id"]==user_logueado[0]["id"]:
                
                    #leer superbloque de particion
                    with open(str(partition["path"]), "rb") as file:
                        file.seek(int(partition["start"]))
                        superblock_infosize =  file.read(struct.calcsize("I I I I I Q Q I I I I I I I I I I"))
                        superblock_unpacked = struct.unpack("I I I I I Q Q I I I I I I I I I I", superblock_infosize)
                        
                        # Obtener los valores desempaquetados del superbloque
                

                        s_filesystem_type = superblock_unpacked[0]
                        s_inodes_count = superblock_unpacked[1]
                        s_blocks_count = superblock_unpacked[2]
                        s_free_blocks_count = superblock_unpacked[3]
                        s_free_inodes_count = superblock_unpacked[4]
                        s_mtime = superblock_unpacked[5]
                        s_umtime = superblock_unpacked[6]
                        s_mnt_count = superblock_unpacked[7]
                        s_magic = superblock_unpacked[8]
                        s_inode_s= superblock_unpacked[9]
                        s_block_s=superblock_unpacked[10]
                        s_first_ino = superblock_unpacked[11]
                        s_first_blo = superblock_unpacked[12]
                        s_bm_inode_start = superblock_unpacked[13]
                        s_bm_block_start = superblock_unpacked[14]
                        s_inode_start = superblock_unpacked[15]
                        s_block_start = superblock_unpacked[16]
                        for variable, valor in locals().items():
                            if variable.startswith('s_'):
                                print(f'{variable} = {valor}')
                        
                        file.seek(int(partition["start"])+s_inode_start)
                        inodoinicial_infosize =  file.read(struct.calcsize('I I I Q Q Q 15i c I'))
                        inodoinicial_unpacked = struct.unpack('I I I Q Q Q 15i c I', inodoinicial_infosize)
                        i_uid = inodoinicial_unpacked[0]
                        i_gid = inodoinicial_unpacked[1]
                        i_s = inodoinicial_unpacked[2]
                        i_atime = inodoinicial_unpacked[3]
                        i_ctime = inodoinicial_unpacked[4]
                        i_mtime = inodoinicial_unpacked[5]
                        i_block = []
                        for i in range (6,21):
                            i_block.append(int(inodoinicial_unpacked[i]))
                    
                        i_type = inodoinicial_unpacked[21].decode('utf-8')
                        i_perm = inodoinicial_unpacked[22]
                        #recorrer i _block eliminar luego
                        

                        # buscar inodo  de usuarios
                        for i in range (0,15):
                            if(search_inodo!=-1):
                                break
                            if(i_block[i]==-1):
                                continue

                            if(i==12): # bloque simple indirecto
                                pos = (int(partition["start"])+s_block_start)+(64*i_block[i])
                                file.seek(int(pos))
                                #leer el bloque apuntador
                                bloqueapuntador_infosize =  file.read(struct.calcsize("16i"))
                                bloqueapuntador_unpacked = struct.unpack("16i", bloqueapuntador_infosize)
                                b_pointers = []
                                for b_pointerValue in range(0,16):
                                    b_pointers.append(bloqueapuntador_unpacked[b_pointerValue])
                        
                                for j in range(0,16):
                                    if(b_pointers[j]==-1):
                                        continue
                                    pos = (int(partition["start"])+s_block_start)+(64*b_pointers[j])
                                    file.seek(pos)
                                    #leer bloque de carpeta
                                    bloquecarpeta_infosize =  file.read(struct.calcsize("12s i 12s i 12s i 12s i"))
                                    carpetasblock = CarpetBlock().unpack(bloquecarpeta_infosize)
                                    for k in range(0,4):
                                        name_carpetblock = getStringWithDot(str(carpetasblock.b_content[k].b_name))
                                        if("users.txt"==str(name_carpetblock)):
                                            search_inodo = carpetasblock.b_content[k].b_inodo
                                            break
                         
                            elif(i==13): #bloque doble indirecto
                                pos = (int(partition["start"])+s_block_start)+(64*i_block[i])
                                file.seek(int(pos))
                                #leer el bloque apuntador
                                bloqueapuntador_infosize =  file.read(struct.calcsize("16i"))
                                bloqueapuntador_unpacked = struct.unpack("16i", bloqueapuntador_infosize)
                                b_pointers = []
                                for b_pointerValue in range(0,16):
                                    b_pointers.append(bloqueapuntador_unpacked[b_pointerValue])

                                for j in range(0,16):
                                    pos = (int(partition["start"])+s_block_start)+(64*i_block[i])
                                    file.seek(int(pos))     
                                    bloqueapuntadord_infosize =  file.read(struct.calcsize("16i"))
                                    bloqueapuntadord_unpacked = struct.unpack("16i", bloqueapuntadord_infosize)
                                    b_pointersd = []
                                    for b_pointerValued in range(0,16):
                                        b_pointersd.append(bloqueapuntadord_unpacked[b_pointerValued])
                                    #--------obtencion de bloque arriba-----
                                    for y in range(0,16):
                                        if(b_pointersd[y]==-1):
                                            continue
                                    
                                        pos = (int(partition["start"])+s_block_start)+(64*b_pointersd[y])
                                        file.seek(int(pos))
                                        #leer el bloque apuntador
                                        bloqueapuntador_infosize =  file.read(struct.calcsize("16i"))
                                        bloqueapuntador_unpacked = struct.unpack("16i", bloqueapuntador_infosize)
                                        b_pointers = []
                                        for b_pointerValue in range(0,16):
                                            b_pointers.append(bloqueapuntador_unpacked[b_pointerValue])
                                
                                        for j in range(0,16):
                                            if(b_pointers[j]==-1):
                                                continue
                                            pos = (int(partition["start"])+s_block_start)+(64*b_pointers[j])
                                            file.seek(pos)
                                            #leer bloque de carpeta
                                            bloquecarpeta_infosize =  file.read(struct.calcsize("12s i 12s i 12s i 12s i"))
                                            carpetasblock = CarpetBlock().unpack(bloquecarpeta_infosize)
                                            for k in range(0,4):
                                                name_carpetblock = getStringWithDot(str(carpetasblock.b_content[k].b_name))
                                                if("users.txt"==str(name_carpetblock)):
                                                    search_inodo = carpetasblock.b_content[k].b_inodo
                                                    break
                            elif(i==14): #bloque triple indirecto
                                    

                                    
                                    pos = (int(partition["start"])+s_block_start)+(64*i_block[i])
                                    file.seek(int(pos))     
                                    bloqueapuntadord_infosize =  file.read(struct.calcsize("16i"))
                                    bloqueapuntadord_unpacked = struct.unpack("16i", bloqueapuntadord_infosize)
                                    b_pointersd = []
                                    for b_pointerValued in range(0,16):
                                        b_pointersd.append(bloqueapuntadord_unpacked[b_pointerValued])
                                    #--------obtencion de bloque arriba-----
                                    for y in range(0,16):
                                        if(b_pointersd[y]==-1):
                                            continue
                                    
                                        pos = (int(partition["start"])+s_block_start)+(64*b_pointersd[y])
                                        file.seek(int(pos))
                                        #leer el bloque apuntador
                                        bloqueapuntador_infosize =  file.read(struct.calcsize("16i"))
                                        bloqueapuntador_unpacked = struct.unpack("16i", bloqueapuntador_infosize)
                                        b_pointers = []
                                        for b_pointerValue in range(0,16):
                                            b_pointers.append(bloqueapuntador_unpacked[b_pointerValue])
                                
                                        for j in range(0,16):
                                            if(b_pointers[j]==-1):
                                                continue

                                            #tercero
                                            pos = (int(partition["start"])+s_block_start)+(64*b_pointers[j])
                                            file.seek(pos)
                                            bloqueapuntador_infosizetercero =  file.read(struct.calcsize("16i"))
                                            bloqueapuntador_unpackedtercero = struct.unpack("16i", bloqueapuntador_infosizetercero)
                                            b_pointerstercero = []
                                            for b_pointerValuetercero in range(0,16):
                                                b_pointerstercero.append(bloqueapuntador_unpackedtercero[b_pointerValuetercero])
                                            for a in range(0,16):
                                                if(b_pointerstercero[a]==-1):
                                                    continue
                                                pos = (int(partition["start"])+s_block_start)+(64*b_pointerstercero[a])
                                                file.seek(pos)
                                                #leer bloque de carpeta
                                                bloquecarpeta_infosize =  file.read(struct.calcsize("12s i 12s i 12s i 12s i"))
                                                carpetasblock = CarpetBlock().unpack(bloquecarpeta_infosize)
                                                for k in range(0,4):
                                                    name_carpetblock = getStringWithDot(str(carpetasblock.b_content[k].b_name))
                                                    if("users.txt"==str(name_carpetblock)):
                                                        search_inodo = carpetasblock.b_content[k].b_inodo
                                                        break
                            else:
                                pos = s_block_start+partition["start"]+(64*i_block[i])
                                file.seek(int(pos))
                                #leer bloque de carpetas
                                bloquecarpeta_infosize =  file.read(struct.calcsize("12s i 12s i 12s i 12s i"))
                                carpetasblock = CarpetBlock().unpack(bloquecarpeta_infosize)
                                for i in range(0,4):
                                        name_carpetblock = getStringWithDot(str(carpetasblock.b_content[i].b_name))
                                        if("users.txt"==str(name_carpetblock)):
                                            search_inodo = carpetasblock.b_content[i].b_inodo
                                           
                                            break
                        #obtener archivo de usuarios
                        leer_file_posicion =  s_inode_start+partition["start"]+(search_inodo*int(getSizeTableInodes()))
                        file.seek(leer_file_posicion)
                        inodoinicial_infosize =  file.read(struct.calcsize('I I I Q Q Q 15i c I'))
                        inodoinicial_unpacked = struct.unpack('I I I Q Q Q 15i c I', inodoinicial_infosize)
                        i_uid = inodoinicial_unpacked[0]
                        i_gid = inodoinicial_unpacked[1]
                        i_s = inodoinicial_unpacked[2]
                        i_atime = inodoinicial_unpacked[3]
                        i_ctime = inodoinicial_unpacked[4]
                        i_mtime = inodoinicial_unpacked[5]
                        i_block = []
                        for i in range (6,21):
                            i_block.append(int(inodoinicial_unpacked[i]))
                    
                        i_type = inodoinicial_unpacked[21].decode('utf-8')
                        i_perm = inodoinicial_unpacked[22]
                        modify_text = ""
                           
                        #leer archivo
                        for i in range (0,15):
                            if(i_block[i]==-1):
                                continue

                            if(i==12): # bloque simple indirecto
                                pos = (int(partition["start"])+s_block_start)+(64*i_block[i])
                                file.seek(int(pos))
                                #leer el bloque apuntador
                                bloqueapuntador_infosize =  file.read(struct.calcsize("16i"))
                                bloqueapuntador_unpacked = struct.unpack("16i", bloqueapuntador_infosize)
                                b_pointers = []
                                for b_pointerValue in range(0,16):
                                    b_pointers.append(bloqueapuntador_unpacked[b_pointerValue])
                        
                                for j in range(0,16):
                                    if(b_pointers[j]==-1):
                                        continue
                                    pos = (int(partition["start"])+s_block_start)+(64*b_pointers[j])
                                    file.seek(pos)
                                    #leer bloque de archivos
                                    bloquearchivo_infosize =  file.read(struct.calcsize("64s"))
                                    archivoblock = struct.unpack("64s", bloquearchivo_infosize)
                                    modify_text += archivoblock[0].decode('utf-8')
                            elif(i==13): #bloque doble indirecto
                                pos = (int(partition["start"])+s_block_start)+(64*i_block[i])
                                file.seek(int(pos))
                                #leer el bloque apuntador
                                bloqueapuntador_infosize =  file.read(struct.calcsize("16i"))
                                bloqueapuntador_unpacked = struct.unpack("16i", bloqueapuntador_infosize)
                                b_pointers = []
                                for b_pointerValue in range(0,16):
                                    b_pointers.append(bloqueapuntador_unpacked[b_pointerValue])

                                for j in range(0,16):
                                    pos = (int(partition["start"])+s_block_start)+(64*i_block[i])
                                    file.seek(int(pos))     
                                    bloqueapuntadord_infosize =  file.read(struct.calcsize("16i"))
                                    bloqueapuntadord_unpacked = struct.unpack("16i", bloqueapuntadord_infosize)
                                    b_pointersd = []
                                    for b_pointerValued in range(0,16):
                                        b_pointersd.append(bloqueapuntadord_unpacked[b_pointerValued])
                                    #--------obtencion de bloque arriba-----
                                    for y in range(0,16):
                                        if(b_pointersd[y]==-1):
                                            continue
                                    
                                        pos = (int(partition["start"])+s_block_start)+(64*b_pointersd[y])
                                        file.seek(int(pos))
                                        #leer el bloque apuntador
                                        bloqueapuntador_infosize =  file.read(struct.calcsize("16i"))
                                        bloqueapuntador_unpacked = struct.unpack("16i", bloqueapuntador_infosize)
                                        b_pointers = []
                                        for b_pointerValue in range(0,16):
                                            b_pointers.append(bloqueapuntador_unpacked[b_pointerValue])
                                
                                        for j in range(0,16):
                                            if(b_pointers[j]==-1):
                                                continue
                                            pos = (int(partition["start"])+s_block_start)+(64*b_pointers[j])
                                            file.seek(pos)
                                            #leer bloque de carpeta
                                            bloquearchivo_infosize =  file.read(struct.calcsize("64s"))
                                            archivoblock = struct.unpack("64s", bloquearchivo_infosize)
                                            modify_text += archivoblock[0].decode('utf-8')
                            elif(i==14): #bloque triple indirecto
                                    

                                    
                                    pos = (int(partition["start"])+s_block_start)+(64*i_block[i])
                                    file.seek(int(pos))     
                                    bloqueapuntadord_infosize =  file.read(struct.calcsize("16i"))
                                    bloqueapuntadord_unpacked = struct.unpack("16i", bloqueapuntadord_infosize)
                                    b_pointersd = []
                                    for b_pointerValued in range(0,16):
                                        b_pointersd.append(bloqueapuntadord_unpacked[b_pointerValued])
                                    #--------obtencion de bloque arriba-----
                                    for y in range(0,16):
                                        if(b_pointersd[y]==-1):
                                            continue
                                    
                                        pos = (int(partition["start"])+s_block_start)+(64*b_pointersd[y])
                                        file.seek(int(pos))
                                        #leer el bloque apuntador
                                        bloqueapuntador_infosize =  file.read(struct.calcsize("16i"))
                                        bloqueapuntador_unpacked = struct.unpack("16i", bloqueapuntador_infosize)
                                        b_pointers = []
                                        for b_pointerValue in range(0,16):
                                            b_pointers.append(bloqueapuntador_unpacked[b_pointerValue])
                                
                                        for j in range(0,16):
                                            if(b_pointers[j]==-1):
                                                continue

                                            #tercero
                                            pos = (int(partition["start"])+s_block_start)+(64*b_pointers[j])
                                            file.seek(pos)
                                            bloqueapuntador_infosizetercero =  file.read(struct.calcsize("16i"))
                                            bloqueapuntador_unpackedtercero = struct.unpack("16i", bloqueapuntador_infosizetercero)
                                            b_pointerstercero = []
                                            for b_pointerValuetercero in range(0,16):
                                                b_pointerstercero.append(bloqueapuntador_unpackedtercero[b_pointerValuetercero])
                                            for a in range(0,16):
                                                if(b_pointerstercero[a]==-1):
                                                    continue
                                                pos = (int(partition["start"])+s_block_start)+(64*b_pointerstercero[a])
                                                file.seek(pos)
                                                #leer bloque de carpeta
                                                bloquearchivo_infosize =  file.read(struct.calcsize("64s"))
                                                archivoblock = struct.unpack("64s", bloquearchivo_infosize)
                                                modify_text += archivoblock[0].decode('utf-8')
                            else:
                                pos = s_block_start+partition["start"]+(64*i_block[i])
                                file.seek(int(pos))
                                #leer bloque de carpetas
                                bloquearchivo_infosize =  file.read(struct.calcsize("64s"))
                                archivoblock = struct.unpack("64s", bloquearchivo_infosize)
                                modify_text += archivoblock[0].decode('utf-8')
                            
                       
                        modify = str(modify_text)
                     
                        line=modify.split("\n")
                        usuarios = [x.split(",") for x in line if len(x.split(",")) == 5]
                        grupos = [x.split(",") for x in line if len(x.split(",")) == 3]
                        
                        #verificar que no exista grupo 
                        GroupFind = False
                        
                        for i in grupos:
                            
                            if str(i[2]) == str(name):
                                    GroupFind= True
                                    break
                        if GroupFind:
                            print("ERROR: El nombre dle grupo a ingresar ya existe")
                            return
                        else:
                            pass

                        numero_bloques = 0
                        for i in grupos:
                            if (str(i[0])!="0"):
                                numero_bloques+=1
                        
                        texto = ""
                        for elemento in line:
                            if not elemento.startswith('\x00'):
                                texto += str(elemento)+"\n"
                        nuevotext = str(numero_bloques+1)+",G,"+str(name)+"\n" 
                        texto += nuevotext
                        
                       
        else:
            print("ERROR: No es posible ejcutar el comando mkgrp, puesto que solo el usuario root puede usarlo")
            
            return
    else:
        print("ERROR: no existe ningun usario logueado para iniciar mkgrp")
        return
    
   # execute -path="/home/user/prueba.eea

