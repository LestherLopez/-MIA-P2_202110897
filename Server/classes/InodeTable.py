import struct
class TablaInodos:
    def __init__(self, i_uid, i_gid, i_s, i_atime, i_ctime, i_mtime, i_block, i_type, i_perm):
        self.i_uid = i_uid #I
        self.i_gid = i_gid #I
        self.i_s = i_s #I
        self.i_atime = i_atime #TIME
        self.i_ctime = i_ctime #TIME
        self.i_mtime = i_mtime #TIME
        self.i_block = i_block #I
        self.i_type = i_type # C
        self.i_perm = i_perm  #I
    def pack(self):
        return struct.pack(
            getFormatTableInodes(), self.i_uid,
                                    self.i_gid,
                                    self.i_s,
                                    self.i_atime,
                                    self.i_ctime, 
                                    self.i_mtime, 
                                    *self.i_block, 
                                    self.i_type.encode('utf-8'), 
                                    self.i_perm
        )


def getFormatTableInodes():
    return 'I I I Q Q Q 15i c I'

def getSizeTableInodes():
 
    return int(struct.calcsize(getFormatTableInodes()))