from nostril import nonsense
import binascii
import string
def c3():
    x = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    tmp = binascii.unhexlify(x)
    for i in string.printable:
        y = ''.join([chr(ord(a)^ord(b)) for (a,b) in zip(tmp, i*len(tmp))])
        if(all(c in string.printable for c in y) and not nonsense(y)):
            print(i,y)
