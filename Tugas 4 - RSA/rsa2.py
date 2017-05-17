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


P_Value = 17
Q_Value = 11

privateKeyD, publicKeyE = get_key(P_Value,Q_Value)
print "Private D : ", privateKeyD
print "Public E : ", publicKeyE

text="mobile suit embeded tactical enforcer"
msg = [ord(c) for c in text]


test = encMessage(msg, publicKeyE)
print test
hasil = decMessage(test, privateKeyD)
print 'ini:',hasil