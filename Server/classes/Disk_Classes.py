import struct
class MBR: 
    def __init__(self, mbr_tamano, mbr_fecha_creacion, mbr_dsk_signature, dsk_fit, mbr_partition_1, mbr_partition_2, mbr_partition_3, mbr_partition_4 ):
        self.mbr_tamano = mbr_tamano
        self.mbr_fecha_creacion = mbr_fecha_creacion
        self.mbr_dsk_signature = mbr_dsk_signature
        self.dsk_fit = dsk_fit
        self.mbr_partition_1 = mbr_partition_1
        self.mbr_partition_2 = mbr_partition_2
        self.mbr_partition_3 = mbr_partition_3
        self.mbr_partition_4 = mbr_partition_4
    def pack(self):
        return struct.pack(
            "I Q I c c c c  I I 16s c c c  I I 16s c c c  I I 16s c c c  I I 16s", 
                self.mbr_tamano, self.mbr_fecha_creacion, self.mbr_dsk_signature,
                self.dsk_fit.encode('utf-8'),
                self.mbr_partition_1.part_status.encode('utf-8'),
                self.mbr_partition_1.part_type.encode('utf-8'),
                self.mbr_partition_1.part_fit.encode('utf-8'),
                self.mbr_partition_1.part_start,
                self.mbr_partition_1.part_s,
                self.mbr_partition_1.part_name.encode('utf-8'),
                self.mbr_partition_2.part_status.encode('utf-8'),
                self.mbr_partition_2.part_type.encode('utf-8'),
                self.mbr_partition_2.part_fit.encode('utf-8'),
                self.mbr_partition_2.part_start,
                self.mbr_partition_2.part_s,
                self.mbr_partition_2.part_name.encode('utf-8'),
                self.mbr_partition_3.part_status.encode('utf-8'),
                self.mbr_partition_3.part_type.encode('utf-8'),
                self.mbr_partition_3.part_fit.encode('utf-8'),
                self.mbr_partition_3.part_start,
                self.mbr_partition_3.part_s,
                self.mbr_partition_3.part_name.encode('utf-8'),
                self.mbr_partition_4.part_status.encode('utf-8'),
                self.mbr_partition_4.part_type.encode('utf-8'),
                self.mbr_partition_4.part_fit.encode('utf-8'),
                self.mbr_partition_4.part_start,
                self.mbr_partition_4.part_s,
                self.mbr_partition_4.part_name.encode('utf-8'),
             
            )




# ESTADOS DE PARTICION
#  0: Inicializado con valores nulos
#  1: ocupado con valores
#  2: particion eliminada
#  3: montada en memoria ram
# 


class Partition:
    def __init__(self, part_status, part_type, part_fit, part_start, part_s, part_name):
        self.part_status = part_status
        self.part_type = part_type
        self. part_fit = part_fit
        self.part_start = part_start       
        self.part_s = part_s                
        self.part_name = part_name


# ESTADOS DE LOGICAS
# 0: Inicializado con valores nulos
# 1: Montada
class EBR:
    def __init__(self, part_status, part_fit, part_start, part_s, part_next, part_name):
        self.part_status = part_status
        self. part_fit = part_fit
        self.part_start = part_start
        self.part_s = part_s
        self.part_next = part_next
        self.part_name = part_name
    def pack(self):
        return struct.pack(
            "c c I I i 16s", 
                self.part_status.encode('utf-8'), 
                self.part_fit.encode('utf-8'),
                self.part_start, 
                self.part_s, 
                self.part_next, 
                self.part_name.encode('utf-8')
             
            )
        