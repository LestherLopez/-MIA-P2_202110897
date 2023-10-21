import struct
class SuperBloque:
    def __init__(self, s_filesystem_type, s_inodes_count, s_blocks_count, s_free_blocks_count, s_free_inodes_count, s_mtime, s_umtime, s_mnt_count, s_magic, s_inode_s, s_block_s, s_first_ino, s_first_blo, s_bm_inode_start, s_bm_block_start, s_inode_start, s_block_start):
        self.s_filesystem_type = s_filesystem_type
        self.s_inodes_count = s_inodes_count
        self.s_blocks_count = s_blocks_count
        self.s_free_blocks_count = s_free_blocks_count
        self.s_free_inodes_count = s_free_inodes_count
        self.s_mtime = s_mtime
        self.s_umtime = s_umtime
        self.s_mnt_count = s_mnt_count
        self.s_magic = s_magic
        self.s_inode_s = s_inode_s
        self.s_block_s = s_block_s
        self.s_first_ino = s_first_ino
        self.s_first_blo = s_first_blo
        self.s_bm_inode_start = s_bm_inode_start
        self.s_bm_block_start = s_bm_block_start
        self.s_inode_start = s_inode_start
        self.s_block_start = s_block_start
    def pack(self):
        return struct.pack(
            getFormatSuperBlock(),  self.s_filesystem_type, 
                                    self.s_inodes_count, 
                                    self.s_blocks_count, 
                                    self.s_free_blocks_count, 
                                    self.s_free_inodes_count, 
                                    self.s_mtime, 
                                    self.s_umtime, 
                                    self.s_mnt_count, 
                                    self.s_magic, 
                                    self.s_inode_s, 
                                    self.s_block_s, 
                                    self.s_first_ino, 
                                    self.s_first_blo, 
                                    self.s_bm_inode_start, 
                                    self.s_bm_block_start, 
                                    self.s_inode_start, 
                                    self.s_block_start
        )

def getFormatSuperBlock():
    return "I I I I I Q Q I I I I I I I I I I"
          
def getSizeSuperBlock():
    return int(struct.calcsize(getFormatSuperBlock()))