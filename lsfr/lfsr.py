
#c = 0xccaa #Taps
#key = 0xfff #Input
#nbits = 64

c = 0x37c54f
key = 0xffff
nbits = 128

c=3639681
key=0xffff
nbits=128

c = format(c, '016b')
key = format(key, '0'+str(len(c))+'b')


print "c  :",c
print "key:", key


while len(key) < nbits:
    i = 0
    xorctr = 0
    for bit in c:
        if bit == "1" and key[i] == "1":
            xorctr +=1
        i+=1
    newBit = str(xorctr % 2)
    key = newBit + key

print "-------"

print "key:", key
print "key:", hex(int(key, 2))

# Reverse
out = ""
buffer = ""
for i in range(0, nbits):
    buffer += key[i]
    if len(buffer) == 8:
        out = buffer + out
        buffer = ""
print "-------"

print "key:", out
print "key:", hex(int(out, 2))