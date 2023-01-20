import usb.core
import usb.util
import time
import sys

class Pdsgo2Dev:
    def getdata(self):
        return '#Rw,     2,     7,     2,     0,     0,   9.8,   8.6,0x00\n\r'


