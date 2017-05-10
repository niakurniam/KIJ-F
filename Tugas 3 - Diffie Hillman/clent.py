import socket
import sys
import enkripsi
import dekripsi

from enkripsi import *
from dekripsi import *

# create socket and connect to server
server_address = ('localhost', 5000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

if (len(sys.argv) < 4):
    print 'Usage : python clent.py prime_number intiger_number private_number'
    sys.exit()

p_number = int(sys.argv[1])
i_number = int(sys.argv[2])
number = int(sys.argv[3])

while True:

    private = (i_number ** number) % p_number
    # print private

    with open('client_key.txt', 'wb') as file:
        pn = file.write(str(private))

    with open('server_key.txt', 'rb') as file:
        pn2 = file.read()
    # print pn2
    # print int(pn2)
    sh = (int(pn2) ** number) % p_number
    sh2 = sh + 10000000
    print 'shared key:', sh2

    try:
        print >> sys.stderr, 'connection from', server_address

        # Receive the data in small chunks and retransmit it
        while True:
            data2 = raw_input('Me: ')
            with open('dataset.txt', 'wb') as f:
                data5 = f.write(data2)
            execfile("enkripsi.py")
            with open('enkripsi.txt', 'rb') as file:
                data6 = file.read()
            client_socket.sendall(data6)

            data = client_socket.recv(1024)
            with open('enkripsi.txt', 'wb') as f:
                data3 = f.write(data)
            execfile("dekripsi.py")
            with open('dekripsi.txt', 'rb') as file:
                data4 = file.read()

            print('server: %s'% data4)
                # print data

    finally:
        print >> sys.stderr, 'closing socket'
        client_socket.close()
