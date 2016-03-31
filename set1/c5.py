import binascii
plaintext = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''

key = 'ICE'

result = ''

for i in range(len(plaintext)):
    result += chr(ord(plaintext[i])^ord(key[i%len(key)]))

print binascii.hexlify(result)
