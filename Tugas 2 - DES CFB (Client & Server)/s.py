import socket #mengimport module socket
import select #mengimport module select
import sys	  #mengimport module sys
import os	  #mengimport module os (digunkan untuk mengambil alamat dari sebuah file) Miscellaneous operating system interfaces

server_address = ('localhost', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address)
server_socket.listen(5)


input_socket = [server_socket]
print "Server sedang berjalan"

try:
    while 1:
        msg=server_socket.recv(1024)
        print msg


except KeyboardInterrupt:
    server_socket.close()
    sys.exit(0)

