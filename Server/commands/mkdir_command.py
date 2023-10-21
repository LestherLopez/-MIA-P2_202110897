import struct
from classes.Superblock import *
from classes.Block import *
from utils.Utils import *
from classes.InodeTable import *
from datetime import datetime
from classes.Journaling import *
def mkdir_command(path, r, user_logueado, list_partitions):
    #verificar que el user logueado sea el root
    print("--------------------------------------------------")
    print("Comando MKDIR en ejecucion...")
    print(f"Path: {path}")
    
    for partition in list_partitions:
            
            if partition["id"]==user_logueado[0]["id"]:
                
                start_partition = partition["start"]
                #leer superbloque de particion
                with open(str(partition["path"]), "rb") as file:
                    file.seek(int(partition["start"]))
                    superblock_infosize =  file.read(struct.calcsize("I I I I I Q Q I I I I I I I I I I"))
                    superblock_unpacked = struct.unpack("I I I I I Q Q I I I I I I I I I I", superblock_infosize)
                    
                    # Obtener los valores desempaquetados del superbloque
            
                    read_inode = 0
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
                    file.seek(int(s_inode_start+start_partition))
                    inodoinicial_infosize =  file.read(struct.calcsize('I I I Q Q Q 15i c I'))
                    inodoinicial_unpacked = struct.unpack('I I I Q Q Q 15i c I', inodoinicial_infosize)
                    i_uid = inodoinicial_unpacked[0] #a
                    i_gid = inodoinicial_unpacked[1]#a
                    i_s = inodoinicial_unpacked[2] #a
                    i_atime =inodoinicial_unpacked[3]
                    i_ctime =inodoinicial_unpacked[4]
                    i_mtime =inodoinicial_unpacked[5]
                    i_block = []
                    for j in range (6,21):
                        i_block.append(int(inodoinicial_unpacked[j]))
                
                    i_type = inodoinicial_unpacked[21].decode('utf-8')
                    i_perm = inodoinicial_unpacked[22]
                    inode =  TablaInodos()
                    inodo_leidos = 0
                    #verificar si carpetas existen
                    continuar_ciclo = True
                    pos = 1
                    if str(ruta) == "/":
                        continuar_ciclo = False
                    contador = 0
                    while(continuar_ciclo):
                        search_inodo = -1
                        inexistent = False
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
                                        if name_carpetblock == path.split('/')[pos]:
                                            #escribir
                                            file.seek(s_inode_start+partition["start"]+(getSizeTableInodes()*inodo_leidos))
                                  
                                            #error
                                            file.write(inodoinicial_infosize)
                                            
                                    
                                            inodo_temp = carpetasblock.b_content[k].b_inodo
                                            
                                            
                                            inodo_leidos = inodo_temp
                                            pos += 1
                               
                                            break
                                    if search_inodo != -1:
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
                                                if name_carpetblock == path.split('/')[pos]:
                                                    #escribir
                                                    file.seek(s_inode_start+partition["start"]+(getSizeTableInodes()*inodo_leidos))
                                        
                                                    #error
                                                    file.write(inodoinicial_infosize)
                                                    
                                            
                                                    inodo_temp = carpetasblock.b_content[k].b_inodo
                                                    
                                                    
                                                    inodo_leidos = inodo_temp
                                                    pos += 1
                                    
                                                    break
                                            if inodo_temp!=-1:
                                                break
                                        if inodo_temp!=-1:
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
                                                    if name_carpetblock == path.split('/')[pos]:
                                                        #escribir
                                                        file.seek(s_inode_start+partition["start"]+(getSizeTableInodes()*inodo_leidos))
                                            
                                                        #error
                                                        file.write(inodoinicial_infosize)
                                                        
                                                
                                                        inodo_temp = carpetasblock.b_content[k].b_inodo
                                                        
                                                        
                                                        inodo_leidos = inodo_temp
                                                        pos += 1
                                        
                                                        break
                                                if inodo_temp!=-1:
                                                    break
                                            if inodo_temp!=-1:
                                                break
                                        if inodo_temp!=-1:
                                            break
                                                    
                            else:
                                pos = s_block_start+partition["start"]+(64*i_block[i])
                                file.seek(int(pos))
                                #leer bloque de carpetas
                                bloquecarpeta_infosize =  file.read(struct.calcsize("12s i 12s i 12s i 12s i"))
                                carpetasblock = CarpetBlock().unpack(bloquecarpeta_infosize)
                                for a in range(0,4):
                                        name_carpetblock = getStringWithDot(str(carpetasblock.b_content[a].b_name))
                                        if name_carpetblock == path.split('/')[pos]:
                                                        #escribir
                                                        file.seek(s_inode_start+partition["start"]+(getSizeTableInodes()*inodo_leidos))
                                            
                                                        #error
                                                        file.write(inodoinicial_infosize)
                                                        
                                                
                                                        inodo_temp = carpetasblock.b_content[a].b_inodo
                                                        
                                                        
                                                        inodo_leidos = inodo_temp
                                                        pos += 1
                                        
                                                        break
                        
                        
                        inexistent= True
                        # crear la carpeta 
                        if(inexistent):
                            contador += 1
                            search_inode = False
                            b_pointerssimple = [-1] * 15
                            b_pointersdoble = [-1] * 15
                            b_pointertriple = [-1] * 15
                            Nouseful_block = 0
                            middle_block = 0
                            #inicializar bloque de carpetas
                            carpetabloque = CarpetBlock()
                            carpetabloque.b_content[0].b_name = "-"
                            carpetabloque.b_content[0].b_inodo = -1
                            carpetabloque.b_content[1].b_name = "-"
                            carpetabloque.b_content[1].b_inodo = -1
                            carpetabloque.b_content[2].b_name="-"
                            carpetabloque.b_content[2].b_inodo = -1
                            carpetabloque.b_content[3].b_name="-"
                            carpetabloque.b_content[3].b_inodo = -1
                            #buscar en simples
                            for i in range(0, 12):
                                if inodo_temp != -1:
                                    break
                                if i_block[i] != -1:
                                    file.seek(partition["start"]+s_block_start+(64*i_block[i]))
                                    bloquecarpeta_infosize =  file.read(struct.calcsize("12s i 12s i 12s i 12s i"))
                                    carpetasblock = CarpetBlock().unpack(bloquecarpeta_infosize)
                                    for k in range(0,4):
                                        name_carpetblock = getStringWithDot(str(carpetasblock.b_content[k].b_name))
                                        search_inodo = carpetasblock.b_content[k].b_inodo
                                        if name_carpetblock == "-":
                                            search_inodo = False
                                            for num in range(0, s_inodes_count):
                                                file.seek(partition["start"]+s_bm_inode_start+num)
                                                bitmap = file.read(1)
                                                if bitmap[0] == 0:
                                                    bitmap[0] = '1'
                                                    inodo_temp = num
                                                    file.seek(partition["start"]+s_bm_inode_start+num)
                                                    file.write(bitmap[0].encode('utf-8'))
                                                    break
                                                if num == s_inodes_count-1:
                                                    return
                                            for num in range(0, s_blocks_count):
                                                file.seek(partition["start"]+s_bm_block_start+num)
                                                bitmap = file.read(1)
                                                if bitmap[0] == 0:
                                                    bitmap[0] = '3'
                                                    Nouseful_block = num
                                                    file.seek(partition["start"]+s_bm_block_start+num)
                                                    file.write(bitmap[0].encode('utf-8'))
                                                    break
                                                if num == s_blocks_count-1:
                                                    return
                                            #escribir bloque de carpetas
                                            file.seek(s_block_start + 64*i_block[i])
                                            carpetabloque.b_content[k].b_name = path.split('/')[pos]
                                            carpetabloque.b_content[k].b_inodo = inodo_temp
                                            serializar = carpetabloque.pack()
                                            file.write(serializar)
                                            s_free_blocks_count -= 1
                                            s_free_inodes_count -= 1
                                            superblock = SuperBloque(s_filesystem_type, s_inodes_count, s_blocks_count, s_free_blocks_count, s_free_inodes_count, s_mtime, s_umtime, s_mnt_count, s_magic, s_inode_s, s_block_s, s_first_ino, s_first_blo, s_bm_inode_start, s_bm_block_start, s_inode_start, s_block_start)
                                            file.seek(int(partition["start"]))
                                            superblock_Serializado = superblock.pack()
                                            file.write(superblock_Serializado)
                                            break
                                else:
                                    search_inode = False
                                    for num in range(0, s_inodes_count):
                                        file.seek(partition["start"]+s_bm_inode_start+num)
                                        bitmap = file.read(1)
                                        if bitmap[0] == 0:
                                            bitmap[0] = '1'
                                            inodo_temp = num
                                            file.seek(partition["start"]+s_bm_inode_start+num)
                                            file.write(bitmap[0].encode('utf-8'))
                                            break
                                        if num == s_inodes_count-1:
                                            return
                                    for num in range(0, s_blocks_count):
                                        file.seek(partition["start"]+s_bm_block_start+num)
                                        bitmap = file.read(1)
                                        if bitmap[0] == 0:
                                            bitmap[0] = '3'
                                            middle_block = num
                                            file.seek(partition["start"]+s_bm_block_start+num)
                                            file.write(bitmap[0].encode('utf-8'))
                                            break
                                        if num == s_blocks_count-1:
                                            return
                                    for num in range(0, s_blocks_count):
                                        file.seek(partition["start"]+s_bm_block_start+num)
                                        bitmap = file.read(1)
                                        if bitmap[0] == 0:
                                            bitmap[0] = '3'
                                            Nouseful_block = num
                                            file.seek(partition["start"]+s_bm_block_start+num)
                                            file.write(bitmap[0].encode('utf-8'))
                                            break
                                        if num == s_blocks_count-1:
                                            return
                                    #escribir bloque de carpetas
                                    file.seek(s_block_start + 64*middle_block)
                                    carpetabloque.b_content[0].b_name = path.split('/')[pos]
                                    carpetabloque.b_content[0].b_inodo = inodo_temp
                                    serializar = carpetabloque.pack()
                                    file.write(serializar)

                                    i_block[i] = middle_block
                                    file.seek(s_inode_start + (getSizeTableInodes()*inodo_leidos))
                                    tablaInodo = TablaInodos(i_uid, i_gid, i_s, i_atime, i_ctime, i_mtime, i_block, i_type, i_perm)
                                    inode_serializado = tablaInodo.pack()
                                    file.write(inode_serializado)
                                    s_free_blocks_count -= 2
                                    s_free_inodes_count -= 1
                                    superblock = SuperBloque(s_filesystem_type, s_inodes_count, s_blocks_count, s_free_blocks_count, s_free_inodes_count, s_mtime, s_umtime, s_mnt_count, s_magic, s_inode_s, s_block_s, s_first_ino, s_first_blo, s_bm_inode_start, s_bm_block_start, s_inode_start, s_block_start)
                                    file.seek(int(partition["start"]))
                                    superblock_Serializado = superblock.pack()
                                    file.write(superblock_Serializado)
                                    break

                    #crear journal si es ext3
                    
                    if (s_filesystem_type==3):
                        comando_ejecutado = "mkdir"
                        ruta = path
                        content = ""
                        fechayhora = int(datetime.now().strftime("%d%m%Y%H%M"))
                        journal1 = Journalingclass(comando_ejecutado, ruta, fechayhora, content)
                        list_journaling.append(journal1)
            

#primera parte            
#execute -path="/home/user/Archivos de Entrada 2S2023/Parte 1/1-crear-discos.adsj"
#execute -path="/home/user/Archivos de Entrada 2S2023/Parte 1/2-crear-particiones.adsj"
#execute -path="/home/user/Archivos de Entrada 2S2023/Parte 1/3-montar-particiones.adsj"
# 4 pendiente
# 5 pendiente
#execute -path="/home/user/Archivos de Entrada 2S2023/Parte 1/6-reportes-parte-1.adsj"
#segunda parte
#execute -path="/home/user/Archivos de Entrada 2S2023/Parte 2/inicio-parte-2.adsj"