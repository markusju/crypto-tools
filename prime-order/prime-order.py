__author__ = 'markus'

p = input("Enter a prime p = ")

buffer = ""

print "p="+str(p)

# Base i: 2 .. p-1
for i in range(2, p):
    # Result of calculation
    res = 0
    # Counter for exponent
    j = 0

    # Repeat until we reach g^i = 1 mod n
    while res != 1:
        # increment j
        j += 1
        # res = (i^j) mod p
        res = (i**j) % p
        buffer += str(res) + " "
    buffer += "-- ord="+str(j)
    print "\t"+ buffer
    buffer = ""

