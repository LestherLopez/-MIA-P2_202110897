import struct
#------Struct bloque de carpetas------
class Content:
    def __init__(self):
        self.b_name = "000000000000"
        self.b_inodo = 0
    def pack(self):
        res = struct.pack("12s i", self.b_name.encode('utf-8'), self.b_inodo)
        return res
    @classmethod
    def unpack(cls, data):
        unpacked = struct.unpack("12s i", data)
        content = cls()
        content.b_name = unpacked[0].decode('utf-8')
        content.b_inodo = unpacked[1]
        return content
class CarpetBlock:
    def __init__(self):
        self.b_content = [Content(), Content(), Content(), Content()]

    def pack(self):
        package = b""
        for i in range(0,4):
            package += self.b_content[i].pack()
        return package
    @classmethod
    def unpack(cls, data):
        carpet_block = cls()
        content_size = struct.calcsize("12s i")
        for i in range(4):
            start = i * content_size
            end = start + content_size
            if end <= len(data):
                content_data = data[start:end]
                carpet_block.b_content[i] = Content.unpack(content_data)
        return carpet_block

def getFormatCarpetBlock():
    return "12s i"
          
def getSizeCarpetBlock():
    return 64
#------Struct bloque de archivos------
class FileBlock:
    def __init__(self, b_content):
        self.b_content = b_content
    def pack(self):
        return struct.pack(getFormatFileBlock(), self.b_content.encode('utf-8'))
def getFormatFileBlock():
    return "64s"
          
def getSizeCarpetBlock():
    return 64



#------Struct bloque de apuntadores------
class PointersBlock:
    def __init__(self, b_pointers):
        self.b_pointers = b_pointers
    def pack(self):
        return struct.pack(getFormatPointersBlock(), self.b_pointers)
def getFormatPointersBlock():
    return "16i"
          
def getSizeCarpetBlock():
    return 64