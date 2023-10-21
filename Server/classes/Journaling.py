import struct
list_journaling = []
class Journalingclass:
    def __init__(self, command, path, datetime, content):
        self.command = command #10s
        self.path = path #40s
        self.datetime = datetime #Q
        self.content = content #120s
    
    def pack(self):
        return struct.pack(getFormatJournaling(),
                           self.command.encode('utf-8'), self.path.encode('utf-8'), self.datetime, self.content.encode('utf-8'))

def getFormatJournaling():
    return '10s 40s Q 120s'

def getSizeJournaling():
    return int(struct.calcsize(getFormatJournaling()))


class MiClasePrincipal:
    def __init__(self):
        self.lista_objetos = []

    def agregar_objeto(self, objeto):
        if isinstance(objeto, Journalingclass):
            self.lista_objetos.append(objeto)
        else:
            print("El objeto no es de la clase correcta.")

    def obtener_objetos(self):
        return self.lista_objetos
