import socket
import sys
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
def encMessage(v_msg, v_e, v_n):
    encMsg = []
    for m in v_msg:
        #print "Huruf : ", m
        c = (m ** v_e) % v_n
        #print c
        encMsg.append(c)
    return encMsg

# Fungsi Dekripsi
def decMessage(v_msg, v_d, v_n):
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

# create socket and connect to server
server_address = ('10.151.44.50', 5000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

if (len(sys.argv) < 3):
    print 'Usage : python clent.py prime_number1 prime_number2'
    sys.exit()

P_Value = int(sys.argv[1])
Q_Value = int(sys.argv[2])
#Find N Value
privateKeyD, publicKeyE = get_key(P_Value,Q_Value)
print "Private D : ", privateKeyD
print "Public E : ", publicKeyE
satu,dua=publicKeyE
tiga,empat=privateKeyD
ksatu=str(satu)
kdua=str(dua)
while True:

    try:
        print >> sys.stderr, 'connection from', server_address
        key = client_socket.recv(1024)
        client_socket.sendall(ksatu)
        nvalue = client_socket.recv(1024)
        client_socket.sendall(kdua)
        nvalue2 = int(nvalue)
        key2 = int(key)

        print "nvalue server adalah: ", nvalue2
        print "public key server adalah: ", key2
        print "percakapan dimulai"
        # Receive the data in small chunks and retransmit it
        while True:

            data2 = raw_input('Me: ')
            if data2:
                msg = [ord(c) for c in data2]
                enk=encMessage(msg,key2,nvalue2)
                data5 = pickle.dumps(enk)
                client_socket.send(data5)

            data = client_socket.recv(1024)
            data6 = pickle.loads(data)
            dek = decMessage(data6, tiga, empat)

            print('server: %s'% dek)
                # print data

    finally:
        print >> sys.stderr, 'closing socket'
        client_socket.close()
