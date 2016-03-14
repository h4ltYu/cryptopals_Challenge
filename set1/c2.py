def c2():
    import binascii
    x1 = '1c0111001f010100061a024b53535009181c'
    x2 = '686974207468652062756c6c277320657965'
    xx1 = binascii.unhexlify(x1)
    xx2 = binascii.unhexlify(x2)
    result = ''.join([chr(ord(a)^ord(b)) for (a,b) in zip(xx1,xx2)])
    return binascii.hexlify(result)
