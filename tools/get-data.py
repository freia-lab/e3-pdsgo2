import usb.core
import usb.util
import time
import sys

reattach = False

dev = usb.core.find(idVendor=0x10c4, idProduct=0xea60)
if dev.is_kernel_driver_active(0):
    reattach = True
    dev.detach_kernel_driver(0)

msg = '#gn\n\r'

#dev.set_configuration(1)

# End of Window's driver set-up. Below follows the set-up when
# the data acquisition program has been started
msg = bytearray()
assert dev.ctrl_transfer(0x41, 0, 0x001, 0, msg) == len(msg)
ret = dev.ctrl_transfer(0xc1, 8, 0x0, 0, 1)
print (ret)
ret = dev.ctrl_transfer(0xc0, 16, 0x0, 0, 19)
print (ret)
msg = bytearray()
assert dev.ctrl_transfer(0x41, 3, 0x0800, 0, msg) == len(msg)
msg = bytearray([0,0,0,0,0,0,0,0,0,0x80,0,0,0,0x20,0,0])
assert dev.ctrl_transfer(0x41, 19, 0x0, 0, msg) == len(msg)
# same as already sent before
msg = bytearray([0,0,0,0,0x11, 0x13])
assert dev.ctrl_transfer(0x41, 25, 0, 6, msg) == len(msg)
msg = bytearray([0,0xc2,1,0])
assert dev.ctrl_transfer(0x41, 30, 0, 4, msg) == len(msg)
msg = bytearray([0,0xc2,1,0])
assert dev.ctrl_transfer(0x41, 30, 0, 4, msg) == len(msg)
#frame 54
msg = bytearray()
assert dev.ctrl_transfer(0x41, 7, 0x0200, 0, msg) == len(msg)
msg = bytearray()
assert dev.ctrl_transfer(0x41, 7, 0x0100, 0, msg) == len(msg)
msg = bytearray()
assert dev.ctrl_transfer(0x41, 3, 0x0800, 0, msg) == len(msg)
msg = bytearray([0x1a,0,0,0x1a,0x11,0x13])
assert dev.ctrl_transfer(0x41, 25, 0, 6, msg) == len(msg)
#frame 62
msg = bytearray([0,0,0,0,0,0,0,0,0x80,0,0,0,0x80,0,0,0])
assert dev.ctrl_transfer(0x41, 19, 0x0, 0, msg) == len(msg)
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
msg = bytearray()
assert dev.ctrl_transfer(0x41, 7, 0x0100, 0, msg) == len(msg)
ret = dev.ctrl_transfer(0xc1, 8, 0x0, 0, 1)
print (ret)
ret = dev.ctrl_transfer(0xc0, 16, 0x0, 0, 19)
print (ret)
ret = dev.ctrl_transfer(0xc1, 8, 0x0, 0, 1)
print (ret)

msg = '#gn\n\r'
assert dev.write(1, msg, 100) == len(msg)
ret = dev.read(0x81, 20, 2000)
sret = ''.join([chr(x) for x in ret])
print (sret)
msg = '#gw\n\r'
assert dev.write(1, msg, 100) == len(msg)
ret = dev.read(0x81, 100, 2000)
sret = ''.join([chr(x) for x in ret])
print (sret)

for j in range (0,30):
    msg = '#gw\n\r'
    assert dev.write(1, msg, 100) == len(msg)
    ret = dev.read(0x81, 100, 2000)
    sret = ''.join([chr(x) for x in ret])
    print (sret)
    time.sleep(1.0)

#if reattach:
#    dev.attach_kernel_driver(0)
quit()

print(dev)
dev.write(1, msg, 100)

print(msg)
ret = dev.read(0x81, 20, 2000)
sret = ''.join([chr(x) for x in ret])
print (sret)
usb.util.dispose_resources(dev)
if reattach:
    dev.attach_kernel_driver(0)
quit()

for j in range (0,30):
    dev.ctrl_transfer(0xc0, 16, 0, 0, 19)
    dev.ctrl_transfer(0xc1, 8, 0, 0, 1)
    dev.write(1, msg, 100)
    for i in range (0,20):
        dev.ctrl_transfer(0xc0, 16, 0, 0, 19)
        dev.ctrl_transfer(0xc1, 8, 0, 0, 1)
        time.sleep(0.03)

    ret = dev.read(0x81, 20, 2000)
    sret = ''.join([chr(x) for x in ret])
    print (sret)
    time.sleep(0.1)
    for i in range (0,20):
        dev.ctrl_transfer(0xc0, 16, 0, 0, 19)
        dev.ctrl_transfer(0xc1, 8, 0, 0, 1)
        time.sleep(0.03)


usb.util.dispose_resources(dev)
if reattach:
    dev.attach_kernel_driver(0)

