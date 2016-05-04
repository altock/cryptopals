__author__ = 'altock'

import base64
import binascii

def hex_to_64(hex):
    bin = binascii.a2b_hex(hex)
    b64 = base64.b64encode(bin)
    return b64

def main():
    # cryptopals hex input string
    hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

    # test if it's working
    b64_answer = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    assert hex_to_64(hex) == b64_answer



if __name__ == "__main__":
    main()