import usb.core
import usb.util
import time
import sys

reattach = False

dev = usb.core.find(idVendor=0x10c4, idProduct=0xea60)

if dev.is_kernel_driver_active(0):
    reattach = True
    print('Active')
    dev.detach_kernel_driver(0)

# Get the serial number
msg = '#gn\n\r'
assert dev.write(1, msg, 100) == len(msg)
ret = dev.read(0x81, 20, 2000)
sret = ''.join([chr(x) for x in ret])
print (sret)

# Read the data
for j in range (0,100):
    msg = '#gw\n\r'
    assert dev.write(1, msg, 100) == len(msg)
    sret =''
    while True: 
        ret = dev.read(0x81, 1000, 2000)
        sret = sret+''.join([chr(x) for x in ret])
        if ret[len(ret)-1] == 0xd:
            print("last char", ret[len(ret)-1])
            break
    print (sret)
    time.sleep(0.1)

if reattach:
    dev.attach_kernel_driver(0)
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

