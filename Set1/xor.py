__author__ = 'altock'
""" Set 1 Challenge 2 of Cryptopals"""


def xor(buf_1, buf_2):
    xor_int = int(buf_1, 16) ^ int(buf_2, 16)
    return hex(xor_int)[2:].strip('L')
    # to get rid of '0x' and "long"
