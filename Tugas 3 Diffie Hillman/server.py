import socket #mengimport module socket
import sys	  #mengimport module sys

server_address = ('localhost', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address)
server_socket.listen(2)

if (len(sys.argv) < 4):
    print 'Usage : python server.py prime_number intiger_number private_number'
    sys.exit()

p_number = int(sys.argv[1])
i_number = int(sys.argv[2])
number = int(sys.argv[3])

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = server_socket.accept()

    private = (i_number ** number) % p_number
    print private
    with open('server_key.txt', 'wb') as file:
        pn = file.write(str(private))

    try:
        print >> sys.stderr, 'connection from', client_address
        with open('client_key.txt', 'rb') as file:
            pn2 = file.read()
        #print pn2
        #print int(pn2)
        sh = (int(pn2) ** number)%p_number
        sh2=sh+10000000
        print 'shared key:', sh2

        with open('sh.txt', 'wb') as file:
            pn2 = file.write(str(sh2))


        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            with open('enkripsi.txt', 'wb') as f:
                data2 = f.write(data)
            execfile("dekripsi.py")
            with open('dekripsi.txt', 'rb') as file:
                data3 = file.read()
            print ('client: %s'% data3)

            data4 = raw_input('Me: ')
            with open('dataset.txt', 'wb') as f:
                data5 = f.write(data4)
            execfile("enkripsi.py")
            with open('enkripsi.txt', 'rb') as file:
                data6 = file.read()
            if data4:
                connection.sendall(data6)
                #print >> sys.stderr, 'no more data from', client_address


    finally:
        # Clean up the connection
        connection.close()