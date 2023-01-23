import usb.core
import usb.util
import time
import sys

class Pdsgo2Dev:

    dev = None

    def init(self, dev):
#        print(self.dev)
        print("========== Initializing USB device ===============\n", dev)
        msg = bytearray()
        assert dev.ctrl_transfer(0x41, 0, 0x001, 0, msg) == len(msg)
        msg = bytearray([0,0xc2,1,0])
        assert dev.ctrl_transfer(0x41, 30, 0, 4, msg) == len(msg)
        msg = bytearray()
        assert dev.ctrl_transfer(0x41, 7, 0x0200, 0, msg) == len(msg)
        msg = bytearray()
        assert dev.ctrl_transfer(0x41, 7, 0x0100, 0, msg) == len(msg)
        msg = bytearray()
        assert dev.ctrl_transfer(0x41, 3, 0x0800, 0, msg) == len(msg)
        msg = bytearray([0x1a,0,0,0x1a,0x11,0x13])
        assert dev.ctrl_transfer(0x41, 25, 0, 6, msg) == len(msg)
        msg = bytearray([0,0,0,0,0,0,0,0,0x80,0,0,0,0x80,0,0,0])
        assert dev.ctrl_transfer(0x41, 19, 0x0, 0, msg) == len(msg)

    def getdata(self):
        if self.dev == None:
            try:
                self.dev = usb.core.find(idVendor=0x10c4, idProduct=0xea60)
                if  self.dev != None:
                     print("PDSGO2 connected")
                     self.init(self.dev)
                     if self.dev.is_kernel_driver_active(0):
                        print('Kernel driver active')
                        self.dev.detach_kernel_driver(0)
                        print('Kernel driver detached')
            except:
                print("PDSGO2 not connected")


        msg = '#gw\n\r'
        assert self.dev.write(1, msg, 100) == len(msg)
        sret =''
        while True: 
            ret = self.dev.read(0x81, 1000, 1500)
            sret = sret+''.join([chr(x) for x in ret])
            if sret.find('#E') != -1:
                print(sret.strip()+'\n\r')
                return sret.strip()+'\n\r'
            if ret[len(ret)-1] == 0xd:
                break
        return sret
#Rw,     2,     7,     2,     0,     0,   9.8,   8.6,0x00\n\r


