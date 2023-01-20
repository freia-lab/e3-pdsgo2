import usb.core
import usb.util
import time
import sys
import socketserver
import socket

from pdsgo2Dev import Pdsgo2Dev


######################################################################
    
#....callback function to handle the connection on the socket
class MyHandler(socketserver.StreamRequestHandler):
    def handle(self):
      pds = Pdsgo2Dev()
      while 1:
        dataReceived = self.rfile.readline() #buffer size in bytes, will split longer messages
        print(dataReceived)
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
        except Exception as e:
            print(e)
        
        print(txt)
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
