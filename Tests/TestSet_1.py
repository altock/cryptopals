__author__ = 'altock'
import unittest

from Set1 import hex_to_64, xor


class TestSetOne(unittest.TestCase):
    # test if it gives valid output to example from CryptoPals in Challenge 1 of Set 1
    def test_hex_to_64_solution(self):
        # cryptopals hex input string
        hex_input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

        # output if it's working
        b64_answer = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

        self.assertEqual(hex_to_64.hex_to_64(hex_input), b64_answer)

    # test if it gives valid output to example from CryptoPals in Challenge 2 of Set 1
    def test_xor_solution(self):
        # cryptopals hex input strings
        hex_1 = "1c0111001f010100061a024b53535009181c"
        hex_2 = "686974207468652062756c6c277320657965"

        # test if it's working
        b64_answer = "746865206b696420646f6e277420706c6179"

        self.assertEqual(xor.xor(hex_1, hex_2), b64_answer)


if __name__ == '__main__':
    unittest.main()
