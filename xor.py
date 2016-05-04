__author__ = 'altock'

import binascii

def xor(buf_1, buf_2):
    xor_int = int(buf_1, 16) ^ int(buf_2, 16)
    return hex(xor_int)[2:].strip('L')
    # to get rid of '0x' and "long"

def main():
    # cryptopals hex input strings
    hex_1 = "1c0111001f010100061a024b53535009181c"
    hex_2 = "686974207468652062756c6c277320657965"

    # test if it's working
    b64_answer = "746865206b696420646f6e277420706c6179"
    #print(xor(hex_1,hex_2))
    assert xor(hex_1, hex_2) == b64_answer

if __name__ == "__main__":
    main()