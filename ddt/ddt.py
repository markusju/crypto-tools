#!/bin/python



def SBOX(inp):
    s_box = {
        0x00: 0x0e,
        0x01: 0x02,
        0x02: 0x01,
        0x03: 0x03,
        0x04: 0x0d,
        0x05: 0x09,
        0x06: 0x00,
        0x07: 0x06,
        0x08: 0x0f,
        0x09: 0x04,
        0x0a: 0x05,
        0x0b: 0x0a,
        0x0c: 0x08,
        0x0d: 0x0c,
        0x0e: 0x07,
        0x0f: 0x0b
    }
    return s_box[inp]


def print_table(table):
    for row in range(len(table)):
        for col in range(len(table[row])):
            print table[row][col],
            if col == len(table[row]) - 1:
                print "\n"


input_legth = 4 # input length of the S-Box in bits
output_length = 4 # output length of the S-Box  in bits

Table = [[0 for x in range(pow(2, input_legth))] for x in range(pow(2,
                                                                    output_length))]  # the table, In is the XOR of the in-going pair, Out is the resulting XOR, the table returns the number of occurences


print_table(Table)
print("---------")

for p1 in range(pow(2, input_legth)):
    c1 = SBOX(p1)
    for p2 in range(pow(2, input_legth)):
        XOR_IN = p1 ^ p2
        XOR_OUT = SBOX(p1) ^ SBOX(p2)
        Table[XOR_IN][XOR_OUT] += 1

print_table(Table)