sbox = {
    0x00: 0x06,
    0x01: 0x04,
    0x02: 0x0c,
    0x03: 0x05,
    0x04: 0x00,
    0x05: 0x07,
    0x06: 0x02,
    0x07: 0x0e,
    0x08: 0x01,
    0x09: 0x0f,
    0x0a: 0x03,
    0x0b: 0x0d,
    0x0c: 0x08,
    0x0d: 0x0a,
    0x0e: 0x09,
    0x0f: 0x0b
}

sboxrev = {v: k for k, v in sbox.iteritems()}


def encrypt(m, k0, k1, k2):
    u = m ^ k0
    v = sbox[u]
    w = v ^ k1
    x = sbox[w]
    c = x ^ k2
    return c


def decrypt(c, k0, k1, k2):
    x = c ^ k2
    w = sboxrev[x]
    v = w ^ k1
    u = sboxrev[v]
    m = u ^ k0
    return m

message = 0xa
M = 3639681

key = M & 0xfff
k2 = key & 0xf
k1 = (key & 0xff) >> 4
k0 = (key & 0xfff) >> 8

print bin(message)

crypt = encrypt(message, k0, k1, k2)
print "crypt:", bin(crypt)
clear = decrypt(crypt, k0, k1, k2)
print "clear:", bin(clear)