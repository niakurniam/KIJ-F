import socket
import sys
import descfb

from descfb import *

while True:
    try:
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ('localhost', 11000)
        #print >> sys.stderr, 'connecting to %s port %s' % server_address
        sock.connect(server_address)
        # Send data
        message2 = raw_input('Key : ')
        with open('key.txt', 'wb') as f1:
            data1 = f1.write(message2)
        message = raw_input('Hakim : ')
        with open('pesan.txt', 'wb') as f2:
            data2 = f2.write(message)
        execfile("descfb.py")
        with open('hasilenkrip.txt', 'rb') as f3:
            data3 = f3.read()
        # with open('hasil.txt', 'rb') as file:
        #     data2 = file.read()
        print >>sys.stderr, 'sending "%s"' % message
        sock.sendall(data3)
        # Look for the response
        data = sock.recv(1024)
        amount_received = 0
        amount_expected = len(data)
        while amount_received < amount_expected:
            # with open('terima2.txt', 'wb') as f:
            #     data3 = f.write(data)
            # execfile("desv4c.py")
            # with open('dekrip2.txt', 'rb') as file:
            #     data4 = file.read()
            amount_received += len(data)
            print >>sys.stderr, 'received "%s"' % data

    finally:
        sock.close()