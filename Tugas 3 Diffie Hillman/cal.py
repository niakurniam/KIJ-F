a=11000        #angka persetujuan kurang dari bilangan prima
b=100153        #angka persetujuan bilangan prima

c=1000        #random number A
f=2017       #random number b


x=(a**c)%b
print x

y=(a**f)%b
print y

x1=(y**c)%b
print x1

y1=(x**f)%b
print y1

#print >> sys.stderr, 'B:"%s"' % data
                #print >> sys.stderr, 'sending data back to the client'

                #print >> sys.stderr, 'no more data from', client_address