from datetime import datetime
import os
import struct
from classes.Disk_Classes import *
from classes.InodeTable import *
import subprocess
from classes.Block import *
from utils.Utils import *
from classes.Journaling import *
textTree = ""
def rep_command(path_option_wc, name_option_wc, id_option_wc, ruta_option, list_mount):
    print("---------------------------------------")
    print("Comando REP en ejecucion con los siguientes parametros:")
    print(f"Path: {path_option_wc}")
    print(f"Id: {id_option_wc}")
    print(f"Name: {name_option_wc}")
    # 7 reportes
    report_functions = {
        "mbr": mbr, #1
        "disk": disk, #2    
        "bm_inode": bm_inode, #3
        "bm_block": bm_block, #4
        "tree": tree, #6
        "sb": sb, #5
        "file": file, #7

    }
    
    report_function = report_functions.get(name_option_wc)
    
    if report_function:
 
        expanded_route = getPath(path_option_wc)
        verifypath(str(expanded_route))
  
        report_function(expanded_route, id_option_wc, ruta_option, list_mount)
    else:
        print("El nombre de reporte no es válido")

def mbr(path_option, id_option_wc, ruta_option, list_mount):
    print("generacion de reporte mbr...")
    #buscar el disk por medio del id
    path_disk = None
    Found = False
    for partition in list_mount:
        if id_option_wc == partition["id"]:
            
            path_disk=str(partition["path"])
            Found=True
    
    if(Found==False):
       print("ERROR: El id ingresado no se encuentra en ningun disk o no esta montada la particion")
       return
    

    with open(str(path_disk), "rb") as file:
        ruta_expandida = path_disk

        if os.path.isfile(str(ruta_expandida)):
            
            # Desempaquetar los datos
            mbr_infosize =  file.read(struct.calcsize('I Q I c c c c  I I 16s c c c  I I 16s c c c  I I 16s c c c  I I 16s'))
            mbr_unpacked = struct.unpack("I Q I c c c c  I I 16s c c c  I I 16s c c c  I I 16s c c c  I I 16s", mbr_infosize)
           
            # Obtener los valores desempaquetados
            mbr_tamano = mbr_unpacked[0]
            mbr_fecha_creacion = mbr_unpacked[1]
          
            fecha_str = str(int(mbr_fecha_creacion))
            fecha_date = datetime.strptime(fecha_str, "%d%m%Y%H%M")
            
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
            file.close() 
    #hacer contrario
   
    f = open('reporte.dot', 'w', encoding="utf-8")
 
    text = 'digraph { \n'
    text += '''graph [rankdir=LR];\n
    node [shape=plaintext];\n

    table [\n
        label=<<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0">\n
            <TR><TD BGCOLOR="darkorchid4"><FONT COLOR="white">REPORTE DE MBR</FONT></TD><TD BGCOLOR="darkorchid4"><FONT COLOR="#000000"> </FONT></TD></TR>\n
            <TR><TD>mbr_tamano</TD><TD>{}</TD></TR>\n
            <TR><TD BGCOLOR="#DDDDDD">mbr_fecha_creacion</TD><TD BGCOLOR="#DDDDDD">{}</TD></TR>\n
            <TR><TD>mbr_disk_signature</TD><TD>{}</TD></TR>\n
        
    \n'''.format(mbr_tamano, fecha_date, mbr_dsk_signature)
    for i in range(0,4):
        if(partitions[i].part_type=='P'):
            name = getString16(partitions[i].part_name)
            text+='''   <TR><TD BGCOLOR="darkorchid4"><FONT COLOR="white">Particion</FONT></TD><TD BGCOLOR="darkorchid4"><FONT COLOR="#000000"> </FONT></TD></TR>\n
                        <TR><TD>part_status</TD><TD>{}</TD></TR>\n
                        <TR><TD BGCOLOR="#DDDDDD">part_type</TD><TD BGCOLOR="#DDDDDD">{}</TD></TR>\n
                        <TR><TD>part_fit</TD><TD>{}</TD></TR>\n
                        <TR><TD BGCOLOR="#DDDDDD">part_start</TD><TD BGCOLOR="#DDDDDD">{}</TD></TR>\n
                        <TR><TD>part_size</TD><TD>{}</TD></TR>\n
                        <TR><TD BGCOLOR="#DDDDDD">part_name</TD><TD BGCOLOR="#DDDDDD">{}</TD></TR>\n
                        \n'''.format(partitions[i].part_status, partitions[i].part_type, partitions[i].part_fit, partitions[i].part_start, partitions[i].part_s, name)
        elif(partitions[i].part_type=='E'):
            name = getString16(partitions[i].part_name)
            text+='''   <TR><TD BGCOLOR="darkorchid4"><FONT COLOR="white">Particion</FONT></TD><TD BGCOLOR="darkorchid4"><FONT COLOR="#000000"> </FONT></TD></TR>\n
                        <TR><TD>part_status</TD><TD>{}</TD></TR>\n
                        <TR><TD BGCOLOR="#DDDDDD">part_type</TD><TD BGCOLOR="#DDDDDD">{}</TD></TR>\n
                        <TR><TD>part_fit</TD><TD>{}</TD></TR>\n
                        <TR><TD BGCOLOR="#DDDDDD">part_start</TD><TD BGCOLOR="#DDDDDD">{}</TD></TR>\n
                        <TR><TD>part_size</TD><TD>{}</TD></TR>\n
                        <TR><TD BGCOLOR="#DDDDDD">part_name</TD><TD BGCOLOR="#DDDDDD">{}</TD></TR>\n
                        \n'''.format(partitions[i].part_status, partitions[i].part_type, partitions[i].part_fit, partitions[i].part_start, partitions[i].part_s, name)
            with open(str(path_disk), "rb+") as file: 
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
                    name = getString16(ebr_name)
        
                    text+='''   <TR><TD BGCOLOR="deeppink1"><FONT COLOR="white">Particion Logica</FONT></TD><TD BGCOLOR="deeppink1"><FONT COLOR="#000000"> </FONT></TD></TR>\n
                            <TR><TD>part_status</TD><TD>{}</TD></TR>\n
                            <TR><TD BGCOLOR="Pink1">part_next</TD><TD BGCOLOR="Pink1">{}</TD></TR>\n
                            <TR><TD>part_fit</TD><TD>{}</TD></TR>\n
                            <TR><TD BGCOLOR="Pink1">part_start</TD><TD BGCOLOR="Pink1">{}</TD></TR>\n
                            <TR><TD>part_size</TD><TD>{}</TD></TR>\n
                            <TR><TD BGCOLOR="Pink1">part_name</TD><TD BGCOLOR="Pink1">{}</TD></TR>\n
                            \n'''.format(ebr_status, ebr_next, ebr_fit, ebr_start, ebr_s, name)
                    if (int(ebr_next)==-1):
                        condicion=False
                        break;
                    else: 
                        condicion = True
                        init = ebr_next

    text += '''</TABLE>>];}\n'''


    f.write(text)
    f.close()
    
    
    subprocess.run(["dot", "-Tjpg", 'reporte.dot', "-o", path_option])
    print("¡Reporte MBR generado con exito!")
def disk(path_option, id_option_wc, ruta_option, list_mount):

    print("generacion de reporte disk...")
    #buscar el disk por medio del id
    path_disk = None
    Found = False
    for partition in list_mount:
        if id_option_wc == partition["id"]:
            
            path_disk=str(partition["path"])
            Found=True
    
    if(Found==False):
       print("ERROR: El id ingresado no se encuentra en ningun disk o no esta montada la particion")
       return
    
    with open(str(path_disk), "rb") as file:
        ruta_expandida = path_disk

        if os.path.isfile(str(ruta_expandida)):
            
            # Desempaquetar los datos
            mbr_infosize =  file.read(struct.calcsize('I Q I c c c c  I I 16s c c c  I I 16s c c c  I I 16s c c c  I I 16s'))
            mbr_unpacked = struct.unpack("I Q I c c c c  I I 16s c c c  I I 16s c c c  I I 16s c c c  I I 16s", mbr_infosize)
           
            # Obtener los valores desempaquetados
            mbr_tamano = mbr_unpacked[0]
            mbr_fecha_creacion = mbr_unpacked[1]
         
            fecha_str = str(int(mbr_fecha_creacion))
            fecha_date = datetime.strptime(fecha_str, "%d%m%Y%H%M")
          
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
            file.close() 
    #hacer contrario
    f = open('reportedsk.dot', 'w', encoding="utf-8")
    percentmbr = getPercentOcupation(125, mbr_tamano)
    text = '''digraph {\n
              rankdir=LR; \n
              subgraph cluster_rectangulo{\n 
             '''
    text += '''
            
            label="";
            margin=5;
            nodesep=0;
            ranksep=0;
            node0[label="MBR", shape=record];
    
    '''

    init = 132
    index = 1
    for i in range(0,4):
        if(partitions[i].part_type=='P'):
            cantidad_espacioLibre = getFreeSpace(init, partitions[i].part_start)
            if cantidad_espacioLibre == 0:
                percentpartition = getPercentOcupation(partitions[i].part_s, mbr_tamano)
                name = getString16(partitions[i].part_name)
                text += f'''node{index} [label="PRIMARIA\\n{percentpartition}%", shape=record];'''
                init = init + partitions[i].part_s
                index = index +1
                #escribir cuadro de particion
            else:
                percenpartition = getPercentOcupation(cantidad_espacioLibre, mbr_tamano)
                text += f'''node{index} [label="LIBRE\\n{percenpartition}%", shape=record];'''
                #escribir espacio libre
                index=index+1
            
        elif(partitions[i].part_type=='E'):
            cantidad_espacioLibre = getFreeSpace(init, partitions[i].part_start)
            if cantidad_espacioLibre == 0:
                percentpartition = getPercentOcupation(partitions[i].part_s, mbr_tamano)
                name = getString16(partitions[i].part_name)
                text += f'''node{index} [label="EXTENDIDA\\n{percentpartition}%'''
                text+='''|{'''
                init = init + partitions[i].part_s
                index=index+1
                with open(str(path_disk), "rb+") as file: 
                    initebr = partitions[i].part_start
                    condicion = True
                    sizelogics = 0
                    while condicion:
                        #ubicarse en donde inicia el ebr
                        file.seek(initebr)
                        ebr_infosize = file.read(struct.calcsize('c c I I i 16s'))
                        ebr_unpacked = struct.unpack('c c I I i 16s', ebr_infosize)
                        ebr_status =  ebr_unpacked[0].decode('utf-8')
                        ebr_fit = ebr_unpacked[1].decode('utf-8')
                        ebr_start = ebr_unpacked[2]
                        ebr_s = ebr_unpacked[3]
                        ebr_next = ebr_unpacked[4]
                        ebr_name = ebr_unpacked[5].decode('utf-8')
                        name = getString16(ebr_name)
                       
                        
                        sizelogics = sizelogics + ebr_s
                        if (int(ebr_next)==-1):
                            #calcular libre
                            if(ebr_status=='0'):
                                text+='''EBR'''
                            else:
                                percent = getPercentOcupation(ebr_s,mbr_tamano)
                                text+='''EBR|'''
                                text+=f'''LOGICA\\n{percent}%'''
                         
                                if((initebr+ebr_s)!=partitions[i].part_s):
                                        percentspace = getPercentOcupation((partitions[i].part_s-sizelogics), mbr_tamano)
                                        text+=f'''|LIBRE\\n{percentspace}%'''
                            condicion=False
                            break;
                        else: 
                            
                            percent = getPercentOcupation(ebr_s, mbr_tamano)
                            text += '''EBR|'''
                            text += f'''LOGICA\\n{percent}%|'''
                        
                                
                            condicion = True
                            initebr = ebr_next
                text += '''}", shape=record];'''
         
                #escribir cuadro de particion
            else:
                percenpartition = getPercentOcupation(cantidad_espacioLibre, mbr_tamano)
                text += f'''node{index} [label="LIBRE\\n{percenpartition}%", shape=record];'''
                index =index+1
                #escribir espacio libre
            #with open
 
    if(init!=mbr_tamano):
        percentspace = getPercentOcupation(mbr_tamano-init, mbr_tamano)
        text += f'''node{index} [label="LIBRE\\n{percentspace}%", shape=record];'''
        index+=1

    for i in range(0, index-1):
        text += f'''node{i} -> node{i+1} [style=invis]\n'''

    text += '''splines=false;\n'''
    text += '}'
# Agrega otra llave de cierre
    text += '}'
    
    f.write(text)
    f.close()
    
    subprocess.run(["dot", "-Tjpg", 'reportedsk.dot', "-o", path_option])
    print("¡Reporte disk creado con exito!")
    print("---------------------------------------")


#1 bloque archivo
#2 bloque de apuntador
#3 bloque de carpeta

        
def bm_inode(path_option, id_option_wc, ruta_option, list_mount):
    print("generacion de reporte bitmap de inodos...")
    #buscar el disk por medio del id
    path_disk = None
    Found = False
    start_partition = None
    size_partition  = None
    for partition in list_mount:
        if id_option_wc == partition["id"]:
            start_partition = partition["start"]
            size_partition = partition["size"]
            path_disk=str(partition["path"])
            Found=True
    
    if(Found==False):
       print("ERROR: El id ingresado no se encuentra en ningun disk o no esta montada la particion")
       return
    
    with open(str(path_disk), "rb") as file:
        ruta_expandida = path_disk
        if os.path.isfile(str(ruta_expandida)):
            file.seek(int(start_partition))
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
            text = ""
            for i in range(0,s_inodes_count):
                file.seek(start_partition+s_bm_inode_start+i)
                superblock_infosize = file.read(1)
                if superblock_infosize[0]==49 :
                    text += "1 "
                elif(superblock_infosize[0]==0):
                    text += "0 "
            f = open(path_option, 'w', encoding="utf-8")
            #acceder a superblock
            f.write(text)
            f.close()
            print("¡Reporte bitmap inodos generado con exito!")
def bm_block(path_option, id_option_wc, ruta_option, list_mount):
    print("generacion de bitmap de blocks...")
    #buscar el disk por medio del id
    path_disk = None
    Found = False
    start_partition = None
    size_partition  = None
    for partition in list_mount:
        if id_option_wc == partition["id"]:
            start_partition = partition["start"]
            size_partition = partition["size"]
            path_disk=str(partition["path"])
            Found=True
    
    if(Found==False):
       print("ERROR: El id ingresado no se encuentra en ningun disk o no esta montada la particion")
       return
    
    with open(str(path_disk), "rb") as file:
        ruta_expandida = path_disk
        if os.path.isfile(str(ruta_expandida)):
            file.seek(int(start_partition))
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
            text = ""
            for i in range(0,s_blocks_count):
                file.seek(start_partition+s_bm_block_start+i)
                superblock_infosize = file.read(1)
                if superblock_infosize[0]==49 or superblock_infosize[0]==50 or superblock_infosize[0]==51:
                    text += "1 "
                elif(superblock_infosize[0]==0):
                    text += "0 "
            f = open(path_option, 'w', encoding="utf-8")
            #acceder a superblock
            f.write(text)
            f.close()
            print("¡Reporte bitmap blocks generado con exito!")
def tree(path_option, id_option_wc, ruta_option, list_mount):
    print("generacion de reporte tree...")
    #buscar el disk por medio del id
    path_disk = None
    Found = False
    start_partition = None
    size_partition  = None
    for partition in list_mount:
        if id_option_wc == partition["id"]:
            start_partition = partition["start"]
            size_partition = partition["size"]
            path_disk=str(partition["path"])
            Found=True
    
    if(Found==False):
       print("ERROR: El id ingresado no se encuentra en ningun disk o no esta montada la particion")
       return
    
    with open(str(path_disk), "rb") as file:
        ruta_expandida = path_disk

        if os.path.isfile(str(ruta_expandida)):
            file.seek(int(start_partition))
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
            textTree = 'digraph { \n'
            textTree += '''graph [rankdir=LR];\n
            node [shape=plaintext];\n'''
            #agregar inodo numero 0
            f = open('reportetree.dot', 'w', encoding="utf-8")
            #acceder a superblock
            f.write(textTree)
            numero_inodo = 0
            principal = ""
            codeInode(file, start_partition, numero_inodo, s_inode_start, principal, s_block_start, f)
            #leer inodo principal
            
            text = "}"
        
            #acceder a superblock
            f.write(text)
            f.close()
            
            subprocess.run(["dot", "-Tpdf", 'reportetree.dot', "-o", path_option])
            textTree = ""
            print("¡Reporte tree generado con exito!")
#inodo->archivodsk, inicio particion, numero de inodo, inicio de inodos, padre, inicio de bloques, archivo graphviz
def codeInode(file, start, numero_inodo, start_inodos, principal, start_bloques, f):
    file.seek(start+start_inodos+(numero_inodo*getSizeTableInodes()))
    inodoinicial_infosize =  file.read(struct.calcsize('I I I Q Q Q 15i c I'))
    inodoinicial_unpacked = struct.unpack('I I I Q Q Q 15i c I', inodoinicial_infosize)
    i_uid = inodoinicial_unpacked[0] #a
    i_gid = inodoinicial_unpacked[1]#a
    i_s = inodoinicial_unpacked[2] #a
    #atime
    if str(int(inodoinicial_unpacked[3]))!="0":
        i_atime = datetime.strptime(str(int(inodoinicial_unpacked[3])), "%d%m%Y%H%M")
    else:
        i_atime =inodoinicial_unpacked[3]
    #ctime
    if str(int(inodoinicial_unpacked[4]))!="0":
        i_ctime = datetime.strptime(str(int(inodoinicial_unpacked[4])), "%d%m%Y%H%M")
    else:
        i_ctime =inodoinicial_unpacked[4]
    #mtime
    if str(int(inodoinicial_unpacked[5]))!="0":
        i_mtime = datetime.strptime(str(int(inodoinicial_unpacked[5])), "%d%m%Y%H%M")
    else:
        i_mtime =inodoinicial_unpacked[5]

    i_block = []
    for j in range (6,21):
        i_block.append(int(inodoinicial_unpacked[j]))

    i_type = inodoinicial_unpacked[21].decode('utf-8')
    i_perm = inodoinicial_unpacked[22]
    text = "Inodo{}".format(numero_inodo)

    text += '''[label=<<TABLE BORDER='2' CELLBORDER='0' CELLSPACING='5' BGCOLOR='indianred'>\n
            <TR><TD colspan='2' PORT='line'><b>Inodo {}</b></TD></TR>\n
            <TR><TD Align='left'>i_uid</TD><TD PORT='line1'>{}</TD></TR>\n
            <TR><TD Align='left' >i_gid</TD><TD PORT='line2'>{}</TD></TR>\n
            <TR><TD Align='left' >size</TD><TD PORT='line3'>{}</TD></TR>\n
            <TR><TD Align='left' >i_atime</TD><TD PORT='line4'>{}</TD></TR>\n
            <TR><TD Align='left' >i_ctime</TD><TD PORT='line5'> {}</TD></TR>\n
            <TR><TD Align='left' >i_mtime</TD><TD PORT='line6'>{}</TD></TR>\n
            <TR><TD Align='left' >i_type</TD><TD PORT='line7'>{}</TD></TR>\n
            <TR><TD Align='left' >i_perm</TD><TD PORT='line8'>{}</TD></TR>\n
            '''.format(numero_inodo, i_uid, i_gid, i_s, i_atime, i_ctime, i_mtime, i_type, i_perm)
    num = 1
    for i in i_block:            
        text += '''<TR><TD Align='left' >i_perm{}</TD><TD PORT='line{}'>{}</TD></TR>\n'''.format(num,(8+num),i)
        num += 1
    text += '''</TABLE>>];\n'''
    if principal != "":
        text += '''{}->Inodo{}:line\n'''.format(principal, numero_inodo)
    f.write(text)
    for i in range(0,15):
        if i_block[i]==-1:
            continue
        principal = "Inodo"+str(numero_inodo)
        """
        if i==12:
            #apuntador->archivodsk, inicio particion, numero de inodo, inicio de inodos, padre, inicio de bloques, numero de bloque, nivel, tipo, archivo graphviz
            codebloqueapuntador(file, start, numero_inodo, start_inodos, principal, start_bloques, i_block[i], 1, i_type, f)
        elif i==13:
            #apuntador->archivodsk, inicio particion, numero de inodo, inicio de inodos, padre, inicio de bloques, numero de bloque, nivel, tipo, archivo graphviz
            codebloqueapuntador(file, start, numero_inodo, start_inodos, principal, start_bloques, i_block[i], 2, i_type, f)
        elif i==14:
            #apuntador->archivodsk, inicio particion, numero de inodo, inicio de inodos, padre, inicio de bloques, numero de bloque, nivel, tipo, archivo graphviz
            codebloqueapuntador(file, start, numero_inodo, start_inodos, principal, start_bloques, i_block[i], 3, i_type, f)
        else:
        """
        if str(i_type) == "1":
            principal += ":line{}".format(8+i+1)
            #archivo->archivodsk, inicio particion, numero de inodo, inicio de inodos, padre, inicio de bloques, numero de bloque, archivo graphviz
            codebloquearchivo(file, start, numero_inodo, start_inodos, principal, start_bloques, i_block[i], f)
        elif str(i_type)== "0":
            principal += ":line{}".format(8+i+1)
            #carpeta->archivodsk, inicio particion, numero de inodo, inicio de inodos, padre, inicio de bloques, numero de bloque,archivo graphviz
            
            codebloquecarpeta(file, start, numero_inodo, start_inodos, principal,  start_bloques, i_block[i], f)
                
#carpeta->archivodsk, inicio particion, numero de inodo, inicio de inodos, padre, inicio de bloques, numero de bloque,archivo graphviz
def codebloquecarpeta(file, start, numero_inodo, start_inodos, principal, start_bloques, nobloque,  f):
    
    file.seek(start_bloques+start+(64*nobloque))
    
    bloquecarpeta_infosize =  file.read(struct.calcsize("12s i 12s i 12s i 12s i"))

    carpetasblock = CarpetBlock().unpack(bloquecarpeta_infosize)
    
    text = "Bloque{}".format(nobloque)
    
    text += "[label = <<TABLE BORDER='2' CELLBORDER='0' CELLSPACING='5' BGCOLOR='white'>\n"
    
    text += "<TR><TD colspan='2' PORT='line'><b>Bloque carpetas {}</b></TD></TR>\n".format(nobloque)
    text += "<TR><TD ><b>b_name</b></TD><TD><b>b_inodo</b></TD></TR>\n"
    for k in range(0,4):
        name_carpetblock = getStringWithDot(str(carpetasblock.b_content[k].b_name))
        
        search_inodo = carpetasblock.b_content[k].b_inodo
        text += "<TR><TD >{}</TD><TD PORT='line{}'>{}</TD></TR>\n".format(name_carpetblock, k+1, search_inodo)
    text += "</TABLE>>];\n"
    text += '''{}->Bloque{}:line\n'''.format(principal,numero_inodo)
    f.write(text)
    
    for i in range(0,4):
        name_carpetblock = getStringWithDot(str(carpetasblock.b_content[k].b_name))
        
        if str(name_carpetblock)==".":
            continue
        elif str(name_carpetblock)=="..":
            continue
        elif int(carpetasblock.b_content[i].b_inodo) == -1:
            continue
        elif int(carpetasblock.b_content[i].b_inodo) == 0:
            continue
        principality = "Bloque{}:line{}".format(nobloque, i+1)
        #inodo->archivodsk, inicio particion, numero de inodo, inicio de inodos, padre, inicio de bloques, archivo graphviz
        codeInode(file, start, carpetasblock.b_content[i].b_inodo, start_inodos, principality, start_bloques, f)

#apuntador->archivodsk, inicio particion, numero de inodo, inicio de inodos, padre, inicio de bloques, numero de bloque, nivel, tipo, archivo graphviz
def codebloqueapuntador(file, start, numero_inodo, start_inodos, principal, start_bloques, nobloque, numero, type, f):
    file.seek(start+start_bloques+(64*nobloque))
    bloqueapuntador_infosize = file.read(struct.calcsize("16i"))
    apuntadorblock = struct.unpack("16i", bloqueapuntador_infosize)
    apuntadores_desempaquetado = []
    for z in range(0,16):
        apuntadores_desempaquetado.append(apuntadorblock[z])
    cadena_numeros = ""
    for j in range(0,16):
        cadena_numeros = str(apuntadores_desempaquetado[j]+",")
    text = "Bloque{}".format(nobloque)
    text += "[label = <<TABLE BORDER='2' CELLBORDER='0' CELLSPACING='5' BGCOLOR='white'>\n"
    text += "<TR><TD><b>Bloque apuntadores {}</b></TD></TR>\n".format(nobloque)
    text += "<TR><TD>{}</TD></TR>".format(cadena_numeros)
    text += "</TABLE>>];\n"
    text += '''{}->Bloque{}'''.format(principal, nobloque)
    f.write(text)

    for i in range(0,16):
       
        if apuntadores_desempaquetado[i]==-1:
            continue
        principal = "Bloque{}".format(i)
        if numero==2:
            #apuntador->archivodsk, inicio particion, numero de inodo, inicio de inodos, padre, inicio de bloques, numero de bloque, nivel, tipo, archivo graphviz
            codebloqueapuntador(file, start, numero_inodo, start_inodos, principal, start_bloques, nobloque, 1, type, f)
        elif numero >= 3:
            codebloqueapuntador(file, start, numero_inodo, start_inodos, principal, start_bloques, nobloque, 2, type, f)
        elif numero==1:
            if str(type) == "1":
                codebloquearchivo(file, start, numero_inodo, start_inodos, principal, start_bloques, apuntadores_desempaquetado[i], f)
            elif str(type) == "0":
                
                codebloquecarpeta(file, start, numero_inodo, start_inodos, principal, start_bloques,apuntadores_desempaquetado[i],  f)


#archivo->archivodsk, inicio particion, numero de inodo, inicio de inodos, padre, inicio de bloques, numero de bloque, archivo graphviz
def codebloquearchivo(file, start, numero_inodo, start_inodos, principal, start_bloques, nobloque, f):
    
    file.seek(start_bloques+start+(64*nobloque))
    bloquearchivo_infosize =  file.read(struct.calcsize("64s"))
    archivoblock = struct.unpack("64s", bloquearchivo_infosize)
    texto_desempaqeutado = archivoblock[0].decode('utf-8')
    modify = str(texto_desempaqeutado)
    cadena = ""
    line=modify.split("\n")
    for elemento in line:
            if not elemento.startswith('\x00'):
                cadena += str(elemento)+"\n"
    text = "Bloque{}".format(nobloque)
    text += "[label = <<TABLE BORDER='2' CELLBORDER='0' CELLSPACING='5' BGCOLOR='white'>\n"
    text += "<TR><TD><b>Bloque archivo {}</b></TD></TR>\n".format(nobloque)
    text += "<TR><TD PORT='line1'>{}</TD></TR>".format(cadena)
    text += "</TABLE>>];\n"
    text += '''{}->Bloque{}\n'''.format(principal, nobloque)
    f.write(text)





def sb(path_option, id_option_wc, ruta_option, list_mount):
   
    print("generacion de reporte sb...")
    #buscar el disk por medio del id
    path_disk = None
    Found = False
    start_partition = None
    size_partition  = None
    for partition in list_mount:
        if id_option_wc == partition["id"]:
            start_partition = partition["start"]
            size_partition = partition["size"]
            path_disk=str(partition["path"])
            Found=True
    
    if(Found==False):
       print("ERROR: El id ingresado no se encuentra en ningun disk o no esta montada la particion")
       return
    
    with open(str(path_disk), "rb") as file:
        ruta_expandida = path_disk

        if os.path.isfile(str(ruta_expandida)):
            
            f = open('reportesb.dot', 'w', encoding="utf-8")
 
            text = 'digraph { \n'
            text += '''graph [rankdir=LR];\n
            node [shape=plaintext];\n

            table [\n
                label=<<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0">\n
                <TR><TD BGCOLOR="deeppink1"><FONT COLOR="white">Reporte de Superbloque</FONT></TD><TD BGCOLOR="deeppink1"><FONT COLOR="#000000"> </FONT></TD></TR>
            \n'''

            file.seek(int(start_partition))
            superblock_infosize =  file.read(struct.calcsize("I I I I I Q Q I I I I I I I I I I"))
            superblock_unpacked = struct.unpack("I I I I I Q Q I I I I I I I I I I", superblock_infosize)
            
            # Obtener los valores desempaquetados del superbloque
            s_filesystem_type = superblock_unpacked[0]
            s_inodes_count = superblock_unpacked[1]
            s_blocks_count = superblock_unpacked[2]
            s_free_blocks_count = superblock_unpacked[3]
            s_free_inodes_count = superblock_unpacked[4]
            s_mtime = datetime.strptime(str(int(superblock_unpacked[5])), "%d%m%Y%H%M")
            if str(int(superblock_unpacked[6]))!="0":
                s_umtime = datetime.strptime(str(int(superblock_unpacked[6])), "%d%m%Y%H%M")
            else:
                s_umtime =superblock_unpacked[6]
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
          
            file.close() 
            for variable, valor in locals().items():
                if variable.startswith('s_'):
                    text += '''<TR><TD BGCOLOR="Pink1">{}</TD><TD BGCOLOR="Pink1">{}</TD></TR>\n'''.format(variable, valor)
                    
            text += '''</TABLE>>];}\n'''

            f.write(text)
            f.close()
            
            subprocess.run(["dot", "-Tpdf", 'reportesb.dot', "-o", path_option])
            print("¡Reporte SB generado con exito!")
   
def file():
    print("file")


def verify_path(path):
    directorio = os.path.dirname(path)
    if not os.path.exists(directorio):
        os.makedirs(directorio)

def getFile():
    print("get file")