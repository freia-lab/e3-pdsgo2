import usb.core
import usb.util
import time
import sys
def printtime():
    t = time.localtime()
    current_time = time.strftime("%Y-%m-%d %H:%M:%S: ", t)
    return(current_time)

reattach = False

dev = usb.core.find(idVendor=0x10c4, idProduct=0xea60)

if dev.is_kernel_driver_active(0):
    reattach = True
    print('Active')
    dev.detach_kernel_driver(0)

# Get the serial number
msg = '#gn\n'
assert dev.write(1, msg, 100) == len(msg)
ret = dev.read(0x81, 20, 2000)
sret = ''.join([chr(x) for x in ret])
print (sret)

# Read the data
for j in range (0,10):
    msg = '#gw\n'
    assert dev.write(1, msg, 100) == len(msg)
    sret =''
#    ret = dev.read(0x81, 1000, 2000)
#    print(ret)
#    sret = sret+''.join([chr(x) for x in ret])
    while True: 
        ret = dev.read(0x81, 1000, 2000)
        sret = sret+''.join([chr(x) for x in ret])
        if ret[len(ret)-1] == 0xd:
            print("last char", ret[len(ret)-1])
            break
    print (printtime()+sret)
    time.sleep(0.1)

#usb.util.dispose_resources(dev)
#if reattach:
#    dev.attach_kernel_driver(0)
