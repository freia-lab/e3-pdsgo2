import usb.core
import usb.util
import time
import sys

reattach = False

dev = usb.core.find(idVendor=0x10c4, idProduct=0xea60)

msg = '#gn\n\r'

# End of Window's driver set-up. Below follows the set-up when
# the data acquisition program has been started
assert dev.ctrl_transfer(0x41, 0, 0x001, 0, None) == 0

assert dev.ctrl_transfer(0x41, 3, 0x0800, 0, None) == 0
msg = bytearray([0,0,0,0,0,0,0,0,0,0x80,0,0,0,0x20,0,0])
assert dev.ctrl_transfer(0x41, 19, 0x0, 0, msg) == len(msg)
msg = bytearray([0,0,0,0,0x11, 0x13])
assert dev.ctrl_transfer(0x41, 25, 0, 6, msg) == len(msg)
msg = bytearray([0,0xc2,1,0])
assert dev.ctrl_transfer(0x41, 30, 0, 4, msg) == len(msg)
msg = bytearray([0,0xc2,1,0])
assert dev.ctrl_transfer(0x41, 30, 0, 4, msg) == len(msg)
#frame 54
msg = bytearray()
assert dev.ctrl_transfer(0x41, 7, 0x0200, 0, None) == 0
assert dev.ctrl_transfer(0x41, 7, 0x0100, 0, None) == 0
assert dev.ctrl_transfer(0x41, 3, 0x0800, 0, None) == 0
msg = bytearray([0x1a,0,0,0x1a,0x11,0x13])
assert dev.ctrl_transfer(0x41, 25, 0, 6, msg) == len(msg)
#frame 62
msg = bytearray([0,0,0,0,0,0,0,0,0x80,0,0,0,0x80,0,0,0])
assert dev.ctrl_transfer(0x41, 19, 0x0, 0, msg) == len(msg)
msg = bytearray([0,0xc2,1,0])
assert dev.ctrl_transfer(0x41, 30, 0, 4, msg) == len(msg)
assert dev.ctrl_transfer(0x41, 7, 0x0200, 0, None) == 0
assert dev.ctrl_transfer(0x41, 7, 0x0100, 0, None) == 0
assert dev.ctrl_transfer(0x41, 3, 0x0800, 0, None) == 0
msg = bytearray([0x1a,0,0,0x1a,0x11,0x13])
assert dev.ctrl_transfer(0x41, 25, 0, 6, msg) == len(msg)
msg = bytearray([0,0,0,0,0,0,0,0,0x80,0,0,0,0x80,0,0,0])
assert dev.ctrl_transfer(0x41, 19, 0x0, 0, msg) == len(msg)
assert dev.ctrl_transfer(0x41, 7, 0x0100, 0, None) == 0
#ret = dev.ctrl_transfer(0xc1, 8, 0x0, 0, 1)
#print (ret)
#ret = dev.ctrl_transfer(0xc0, 16, 0x0, 0, 19)
#print (ret)
#ret = dev.ctrl_transfer(0xc1, 8, 0x0, 0, 1)
#print (ret)
