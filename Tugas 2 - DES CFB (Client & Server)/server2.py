import socket
import sys
import descfb1
# # import desv4k
# #
# # from desv4s import *
from descfb1 import *

server_address = ('localhost', 11000)
print >> sys.stderr, 'starting up on %s port %s' % server_address

# Listen for incoming connections
while True:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind(server_address)
    sock.listen(1)

    # Wait for a connection
    # print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

    try:
        print >>sys.stderr, 'connection from', client_address
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            with open('terima.txt', 'wb') as f:
                data1 = f.write(data)
            execfile("descfb1.py")

            print >>sys.stderr, 'received "%s"' % data1
            if data1:
                message = raw_input('nia : ')
                print >> sys.stderr, 'sending "%s"' % message
                #print >>sys.stderr, 'sending data back to the client'
                connection.sendall(message)
            else:
                print >>sys.stderr, 'no more data from', client_address
            break
    finally:
        # Clean up the connection
        connection.close()