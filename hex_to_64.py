__author__ = 'altock'
""" Set 1 Challenge 1 of Cryptopals"""

import base64
import binascii


def hex_to_64(hex):
    """
    Converts hex input strings into base 64 binary bytes
    :param hex: hex input string, formatted as "0000AAAA" for example
    :return: bytes string in base 64
    """
    bin = binascii.a2b_hex(hex)
    b64 = base64.b64encode(bin)

    assert isinstance(b64, bytes)
    return b64
