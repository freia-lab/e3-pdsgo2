import usb.core
import usb.util
import time
import sys
import socketserver
import socket
import binascii
import struct

from streamDevSrv import StreamDevSrv


def main():

    port = 1140

    srv = StreamDevSrv(port)

    print("\n*** Using port: ",port, " ***")

    srv.run()

if __name__ == "__main__":
    main()
