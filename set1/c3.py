def c3():
    import binascii
    import string
    x = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    tmp = binascii.unhexlify(x)
    for i in string.printable:
        print (i, ''.join([chr(ord(a)^ord(b)) for (a,b) in zip(tmp, i*len(tmp))]))
