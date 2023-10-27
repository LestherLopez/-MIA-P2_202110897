from classes.Superblock import *
from classes.InodeTable import *
from classes.Journaling import *
from classes.State import *
from classes.Block import *
import math
from datetime import datetime
import sys
def mkfs_command(id_option, type_option, fs_option, list_mount, list_users):
    print("---------------------------------------")
    print("Comando MKFS en ejecucion con los siguientes parametros:")
    print(f"Id: {id_option}")
    print(f"Type: {type_option}")
    print(f"fs: {fs_option}")
    find = False
    path_dsk = None
    partition_size = None
    partition_start = None
    for partition in list_mount:
        if id_option == partition["id"]:
            path_dsk = partition["path"]
            partition_size = partition["size"]
            partition_start = partition["start"]
            find = True
            
    if find:
        pass
    else:
        print(f"Particion {id_option} no encontrado en las particiones montadas, por lo que no es posible ejecutar mkfs.")
        estado.mensaje = f"ERROR: Particion {id_option} no encontrado en las particiones montadas, por lo que no es posible ejecutar mkfs."
        return
    n = None
    numeros_Estructuras = None
    superblock_size = getSizeSuperBlock()
    table_inodes_size = getSizeTableInodes()
    block_size = 64
    Journalingsize = getSizeJournaling()
    #escritura de superbloque
    if(fs_option=='2fs'):
        print("---Creacion de sistema EXT2---")
        
        #Superbloque ->  bitmap inodos -> bitmap bloques -> inodos -> bloques
        n = (int(partition_size) - int(superblock_size)) / (1 + 3 + int(table_inodes_size) + 3 * int(block_size))
        numeros_Estructuras = int(math.floor(n))
        s_filesystem_type = 2
        s_inodes_count = numeros_Estructuras
        s_blocks_count = numeros_Estructuras*3
        s_free_blocks_count = int(numeros_Estructuras-2)
        s_free_inodes_count = int(numeros_Estructuras*3-2)
        s_mtime = int(datetime.now().strftime("%d%m%Y%H%M"))
        s_umtime = 0
        s_mnt_count = 1
        s_magic = 0xEF53
        s_inode_s = table_inodes_size
        s_block_s = 64
        s_first_ino = int(superblock_size+s_inodes_count+s_blocks_count+(2*table_inodes_size)) 
        s_first_blo = int(superblock_size+s_inodes_count+s_blocks_count+(s_inodes_count*table_inodes_size)+(2*64))
        s_bm_inode_start = int(superblock_size) #inicio de bitmap de inodos (partition_Start)
        s_bm_block_start = int(superblock_size+s_inodes_count) #inicio de bitma bloques
        s_inode_start = int(s_bm_block_start+s_blocks_count) #inicio de inodos
        s_block_start = int(s_inode_start+(s_inodes_count*table_inodes_size)) #inicio de bloques
        superblock = SuperBloque(s_filesystem_type, s_inodes_count, s_blocks_count, s_free_blocks_count, s_free_inodes_count, s_mtime, s_umtime, s_mnt_count, s_magic, s_inode_s, s_block_s, s_first_ino, s_first_blo, s_bm_inode_start, s_bm_block_start, s_inode_start, s_block_start)
        patron_variable = "s_"


        with open(str(path_dsk), "rb+") as file: 
            file.seek(int(partition_start))
            superblock_Serializado = superblock.pack()
            file.write(superblock_Serializado)
            file.close()
    elif(fs_option=='3fs'):
        estado.mensaje = "ERROR: Unicamente se permite hacer formateo ext2"
        return
        
    if(n<=0):
        print("ERROR: No existe suficiente espacio en la particion para realizar el formateo")
        estado.mensaje = "ERROR: No existe suficiente espacio en la particion para realizar el formateo"
        return
    else: 
        pass
    #write first block and inode in bitmap
    with open(str(path_dsk), "rb+") as file: 
            numberonoe = '3'
            file.seek(int(partition_start+s_bm_block_start))
            file.write(numberonoe.encode('utf-8'))
            file.seek(int(partition_start+s_bm_inode_start))
            numberonoe = '1'
            file.write(numberonoe.encode('utf-8'))
            file.close()
        
    #inicializar tabla de inodos
    i_uid = 1
    i_gid = 1
    i_s = 0
    i_atime = 0
    i_ctime = int(datetime.now().strftime("%d%m%Y%H%M"))
    i_mtime = int(datetime.now().strftime("%d%m%Y%H%M"))
    i_block = [0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    i_type = "0"
    i_perm = 777
    tablaInodo = TablaInodos(i_uid, i_gid, i_s, i_atime, i_ctime, i_mtime, i_block, i_type, i_perm)
    with open(str(path_dsk), "rb+") as file: 
            file.seek(int(partition_start+s_inode_start))
            inode_serializado = tablaInodo.pack()
            file.write(inode_serializado)
            file.close()
    

    #inicializar bloque de carpetas
    carpetabloque = CarpetBlock()
    carpetabloque.b_content[0].b_name = "."
    carpetabloque.b_content[0].b_inodo = 0
    carpetabloque.b_content[1].b_name = ".."
    carpetabloque.b_content[1].b_inodo = 0
    carpetabloque.b_content[2].b_name="users.txt"
    carpetabloque.b_content[2].b_inodo = 1
    
    with open(str(path_dsk), "rb+") as file: 
            file.seek(int(partition_start+s_block_start))
            serializar = carpetabloque.pack()
            file.write(serializar)
            file.close()
    #marcar nuevamente en bitmap de bloques
    with open(str(path_dsk), "rb+") as file: 
            numberonoe = '1'
            size_char = sys.getsizeof(numberonoe.encode('utf-8'))
          #  print(size_char)
            file.seek(int(partition_start+s_bm_block_start)+1)
            file.write(numberonoe.encode('utf-8'))
            file.seek(int(partition_start+s_bm_inode_start)+1)
            file.write(numberonoe.encode('utf-8'))
            file.close()
    #inicializar bloque de archivos
    b_content = "1,G,root\n1,U,root,root,123\n"
    archivobloque = FileBlock(b_content)
    with open(str(path_dsk), "rb+") as file: 
            file.seek(int(partition_start+s_block_start+64))
            archivobloque_serializado = archivobloque.pack()
            file.write(archivobloque_serializado)
            file.close()

    if s_filesystem_type == 3:
        
         comando_ejecutado = "mkdir"
         path = "/"
         contenido = ""
         datetimea = int(datetime.now().strftime("%d%m%Y%H%M"))
         journal1 = Journalingclass(comando_ejecutado, path, datetimea, contenido)
         list_journaling.append(journal1)
         comando_ejecutado2 = "mkfile"
         path2 = "/"
         contenido2 = "users.txt"
         datetime2 = int(datetime.now().strftime("%d%m%Y%H%M"))
         journal2 = Journalingclass(comando_ejecutado2, path2, datetime2, contenido2)
         list_journaling.append(journal2)
    else:
         pass

    #inodo del archivo
    i_uid = 1
    i_gid = 1
    i_s = 64
    i_atime = 0
    i_ctime = int(datetime.now().strftime("%d%m%Y%H%M"))
    i_mtime = int(datetime.now().strftime("%d%m%Y%H%M"))
    i_block = [1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    i_type = "1"
    i_perm = 777
    tablaInodo = TablaInodos(i_uid, i_gid, i_s, i_atime, i_ctime, i_mtime, i_block, i_type, i_perm)
    with open(str(path_dsk), "rb+") as file: 
            file.seek(int(partition_start+s_inode_start+table_inodes_size))
            inode_serializado = tablaInodo.pack()
            file.write(inode_serializado)
            file.close()
    list_users.append({"user":'root', "password": '123'})
    #escribir journal si es ext3
    
    
    print("Particion formateada de manera correcta")
    estado.mensaje = "¡Particion formateada de manera correcta!"
    print("---------------------------------------")

#execute -path="/home/user/prueba.eea

