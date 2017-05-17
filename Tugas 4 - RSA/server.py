<<<<<<< HEAD
import socket #mengimport module socket
import sys	  #mengimport module sys
import pickle
from fractions import gcd
import random

def intcaststr(bitlist):
    return int("".join(str(i) for i in bitlist), 2)

def bitfield(n):
    return [1 if digit=='1' else 0 for digit in bin(n)[2:]]

def str_ke_bitlist(s):
    ords = (ord(c) for c in s)
    shifts = (7, 6, 5, 4, 3, 2, 1, 0)
    return [(o >> shift) & 1 for o in ords for shift in shifts]

def bitlist_ke_chars(bl):
    bi = iter(bl)
    bytes = zip(*(bi,) * 8)
    shifts = (7, 6, 5, 4, 3, 2, 1, 0)
    for byte in bytes:
        yield chr(sum(bit << s for bit, s in zip(byte, shifts)))

def bitlist_ke_str(bl):
    return ''.join(bitlist_ke_chars(bl))


def multiplicative_inverse(e, euler):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_euler = euler

    while e > 0:
        temp1 = temp_euler / e
        temp2 = temp_euler - temp1 * e
        temp_euler = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_euler == 1:
        return d + euler


def get_key(p, q):
    # n = pq
    n = p * q

    # euler is the totient of n
    euler = (p - 1) * (q - 1)

    # Choose an integer e such that e and euler(n) are coprime
    e = random.randrange(1, euler)

    # Use Euclid's Algorithm to verify that e and euler(n) are comprime
    g = gcd(e, euler)
    while g != 1:
        e = random.randrange(1, euler)
        g = gcd(e, euler)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, euler)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)

    #print "nilai e: ", e
    #print "nilai d: ", d
    #print "nilai n: ", n
    return ((e, n), (d, n))


# Mengenkripsi kalimat
def encMessage(v_msg, key):
    v_e, v_n=key
    encMsg = []
    for m in v_msg:
        #print "Huruf : ", m
        c = (m ** v_e) % v_n
        #print c
        encMsg.append(c)
    return encMsg

# Fungsi Dekripsi
def decMessage(v_msg, key):
    v_d, v_n=key
    decMsg = []
    decString = ''
    for m in v_msg:
        #print "Encript : ", m
        dec = (m ** v_d) % v_n
        #print "Dec : ", dec
        strDec = chr(dec)
        decString+=strDec
        # print strDec
        decMsg.append(dec)
    print "Result : ", decString
    return decString

# server_address = ('localhost', 5000)
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server_socket.bind(server_address)
# server_socket.listen(2)


P_Value = int(raw_input("masukkan bilangan prima q (17, 19, 23): "))
Q_Value = int(raw_input("Masukkan bilangan prima p harus berbeda dengan bilangan q: "))

# P_Value = int(sys.argv[1])
# Q_Value = int(sys.argv[2])
#Find N Value
privateKeyD, publicKeyE = get_key(P_Value,Q_Value)
print "Private D : ", privateKeyD
print "Public E : ", publicKeyE
str1 = str(publicKeyE[0])
str2 = str(publicKeyE[1])

strr=(str1,str2)

while True:
    server_address = ('localhost', 7000)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(server_address)
    server_socket.listen(1)

    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = server_socket.accept()
    satu1=pickle.dumps(strr)
    connection.send(satu1)
    value = connection.recv(1024)
    cek = pickle.loads(value)

    p1 = int(cek[0])
    q1 = int(cek[1])

    global publicc
    publicc = (p1, q1)
    print "nvalue server adalah: "
    print "public key client adalah: ",publicc

    try:
        while True:
            print "percakapan dimulai"
            data = connection.recv(1024)
            terima = pickle.loads(data)
            pesan = decMessage(terima, privateKeyD)
            print ('client: %s'% pesan)

            data4 = raw_input('Me: ')

            if data4:
                enk = encMessage(data4, k)
                kirim = pickle.dumps(enk)
                connection.send(kirim)
                #print >> sys.stderr, 'no more data from', client_address


    finally:
        # Clean up the connection
        connection.close()
=======
import socket #mengimport module socket
import sys	  #mengimport module sys
import pickle
from fractions import gcd
import random

def intcaststr(bitlist):
    return int("".join(str(i) for i in bitlist), 2)

def bitfield(n):
    return [1 if digit=='1' else 0 for digit in bin(n)[2:]]

def str_ke_bitlist(s):
    ords = (ord(c) for c in s)
    shifts = (7, 6, 5, 4, 3, 2, 1, 0)
    return [(o >> shift) & 1 for o in ords for shift in shifts]

def bitlist_ke_chars(bl):
    bi = iter(bl)
    bytes = zip(*(bi,) * 8)
    shifts = (7, 6, 5, 4, 3, 2, 1, 0)
    for byte in bytes:
        yield chr(sum(bit << s for bit, s in zip(byte, shifts)))

def bitlist_ke_str(bl):
    return ''.join(bitlist_ke_chars(bl))


def multiplicative_inverse(e, euler):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_euler = euler

    while e > 0:
        temp1 = temp_euler / e
        temp2 = temp_euler - temp1 * e
        temp_euler = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_euler == 1:
        return d + euler


def get_key(p, q):
    # n = pq
    n = p * q

    # euler is the totient of n
    euler = (p - 1) * (q - 1)

    # Choose an integer e such that e and euler(n) are coprime
    e = random.randrange(1, euler)

    # Use Euclid's Algorithm to verify that e and euler(n) are comprime
    g = gcd(e, euler)
    while g != 1:
        e = random.randrange(1, euler)
        g = gcd(e, euler)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, euler)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)

    #print "nilai e: ", e
    #print "nilai d: ", d
    #print "nilai n: ", n
    return ((e, n), (d, n))


# Mengenkripsi kalimat
def encMessage(v_msg, key):
    v_e, v_n=key
    encMsg = []
    for m in v_msg:
        #print "Huruf : ", m
        c = (m ** v_e) % v_n
        #print c
        encMsg.append(c)
    return encMsg

# Fungsi Dekripsi
def decMessage(v_msg, key):
    v_d, v_n=key
    decMsg = []
    decString = ''
    for m in v_msg:
        #print "Encript : ", m
        dec = (m ** v_d) % v_n
        #print "Dec : ", dec
        strDec = chr(dec)
        decString+=strDec
        # print strDec
        decMsg.append(dec)
    print "Result : ", decString
    return decString

server_address = ('localhost', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address)
server_socket.listen(2)

if (len(sys.argv) < 3):
    print 'Usage : python server.py prime_number1 prime_number2'
    sys.exit()

P_Value = int(sys.argv[1])
Q_Value = int(sys.argv[2])
#Find N Value
privateKeyD, publicKeyE = get_key(P_Value,Q_Value)
print "Private D : ", privateKeyD
print "Public E : ", publicKeyE
satu=str(publicKeyE)
type (publicKeyE)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = server_socket.accept()
    satu1=pickle.dumps(satu)
    connection.send(satu1)
    
    try:
        print >> sys.stderr, 'connection from', client_address
        value=connection.recv(1024)
        k = pickle.loads(value)
        #nvalue,key=str(value)
        #nvalue2 = ''
        #key2 = ''
        #for nvalue2, key2 in k.iteritems():
        #    nvalue2, key2=k
        x=len(k)
        print 'ini x', x
        t1 = k.strip('(')
        t2= t1.strip(')')
        t3=t2.strip(',')
        print t3
        T9 = map(int, t3)
        nvalue2, key2 = T9
        print "nvalue client adalah: ", nvalue2
        print "public key client adalah: ", key2
        print "percakapan dimulai"
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            terima = pickle.loads(data)
            pesan = decMessage(terima, privateKeyD)
            print ('client: %s'% pesan)

            data4 = raw_input('Me: ')

            if data4:
                enk = encMessage(data4, k)
                kirim = pickle.dumps(enk)
                connection.send(kirim)
                #print >> sys.stderr, 'no more data from', client_address


    finally:
        # Clean up the connection
        connection.close()
>>>>>>> 56046b48624fdecd309ed30860e7ac7e89be66e7
