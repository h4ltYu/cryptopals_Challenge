from nostril import nonsense
import binascii
import string
def c3(x):
    tmp = binascii.unhexlify(x)
    res = []
    for i in string.printable:
        y = ''.join([chr(a^ord(b)) for (a,b) in zip(tmp, i*len(tmp))])
        if(all(c in string.printable for c in y) and not nonsense(y)):
            res.append((i,y.strip()))
    return res
lines = open('4.txt').readlines()
for i in range(len(lines)):
    res = c3(lines[i].strip())
    if len(res)>0:
        for x in res:
            print("Line: %d - %s - \"%s\"" %(i, x[0],x[1]))
