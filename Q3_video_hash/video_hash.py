#!/usr/bin/env python3

from Crypto.Hash import SHA256
import os
import sys

def fileHash(filename:str)->bytes:
    """Return hash value of a file"""
    file=open(filename,'rb')
    f_size=os.path.getsize(filename)
    if f_size/1024==0:
        seek_pos=f_size-1024
    else:
        seek_pos=f_size-f_size%1024
    block=None
    blocks=[]
    hash_val=bytes()
    while seek_pos>=0:
        file.seek(seek_pos)
        block=file.read(1024)+hash_val
        blocks.append(block)
        hash_val=SHA256.new(block).digest()
        seek_pos-=1024
    blocks.reverse()
    return hash_val,blocks

class PseudoReceive:
    blocks=[]
    nBlock=0
    hash_val=None
    curent_receive_index=-1
    def __init__(self,filename:str):
        """Initialize pseudo receive instance object."""
        self.hash_val,self.blocks=fileHash(filename)
        self.nBlock=len(self.blocks)
        self.curent_receive_index=-1

    def receiveNextBlock(self):
        self.curent_receive_index+=1
        if self.curent_receive_index>=len(self.blocks):
            print("Succesfully receive all blocks")
            return self.curent_receive_index,None
        print("Receive block number ",self.curent_receive_index)
        return self.curent_receive_index,self.blocks[self.curent_receive_index]
    def getHashVal(self):
        return self.hash_val

def pseudoVerify(pseudoReceive:PseudoReceive)->bool:
    hash_val=pseudoReceive.getHashVal()
    while(True):
        cur_index,block=pseudoReceive.receiveNextBlock()
        if block is None:
            print("Verified status: OK")
            return True
        if hash_val==SHA256.new(block).digest():
            print("Verify block number",cur_index,": OK\n")
            hash_val=block[-32:]
        else:
            print("verified status: ERROR")
            return False

def main():
    filename=sys.argv[1]
    recv=PseudoReceive(filename)
    pseudoVerify(recv)
    print("HASH VALUE h0 is:\n",fileHash(filename)[0].hex())

if __name__=='__main__':
    main()






    



    