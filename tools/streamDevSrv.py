import usb.core
import usb.util
import time
import sys
import socketserver
import socket

from pdsgo2Dev import Pdsgo2Dev

pds = None

######################################################################
    
#....callback function to handle the connection on the socket
class MyHandler(socketserver.StreamRequestHandler):

    def printtime(self):
        t = time.localtime()
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
        return(current_time)

    def handle(self):
      global pds
      print("pds:",pds)
      if pds == None:
        print("Created instance of Pdsgo2Dev")
        pds = Pdsgo2Dev()
      while 1:
        dataReceived = self.rfile.readline() #buffer size in bytes, will split longer messages
#        print(dataReceived)
        if not dataReceived: break
        request=dataReceived.decode()
#        print(request)
        
        res=request.split()
#        print (res, res[0])
        txt="?\n"
        
        try:
            #ind=int(res[1])
            #ind=1
            #print(ind)
            if res[0]=="#gw":
                txt = pds.getdata() 
        except usb.core.USBTimeoutError:
            print(self.printtime()+" - USB time-out")
        except usb.core.USBError:
            pds.dev = None
            print("USBError:", usb.core.USBError)
            print("PDSGO2 disconnected")
        except Exception as e:
            if pds.dev != None:
                print(e)
        
#        print(txt)
        self.wfile.write(txt.encode())

# https://stackoverflow.com/a/18858817        
class MyTCPServer(socketserver.TCPServer):
    def server_bind(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)


class StreamDevSrv:
    debug = 1
    myserver = None

    def __init__(self, port):
        self.myserver = MyTCPServer(("", port), MyHandler)

 
    def setDebugLvl(self, level):
        self.debug = level

    def run(self):
        try:
            self.myserver.serve_forever()
        except KeyboardInterrupt:
            #            cleanup()
            print("Ctrl-c user exit. \nClosing all devices...")
            sys.exit()
