#!/usr/bin/env python3
#dec2bin.py decimal to binary conversion


def dec2bin(n):
        # bs is the binary string
        binValue = bin(n)
        bs = str(bin(n))
        b = bs.replace('0b','')
        return b # b is a string

def main():
        bString = dec2bin(10)
        print("\t",10, bString)
        bString = dec2bin(245)
        print("\t",245, bString)
        bString = dec2bin(65521)
        print("\t",65521, bString)
        bString = dec2bin(1023)
        print("\t",1023, bString)
main()