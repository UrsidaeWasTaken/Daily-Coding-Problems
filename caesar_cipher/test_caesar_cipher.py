import unittest
from caesar_cipher import caesar_cipher

class TestCaesarCipher(unittest.TestCase):

    def test_cipher(self):
        # My test inputs are stored in a list as it's faster to write and more concise
        plaintexts = ["self", "CONFIDENTIAL!!!", "One, 2, Three, Four, 5", "abcdefghijklmnopqrstuvwxyz", "5", "Plaintext"]
        encrypts = [5, 20, 8, 15, 10, 0]
        answers = ["xjqk", "WIHZCXYHNCUF!!!", "Wvm, 2, Bpzmm, Nwcz, 5", "pqrstuvwxyzabcdefghijklmno", "5", "Plaintext"]

        for plaintext, encrypt, answer in zip(plaintexts, encrypts, answers):
            self.assertEqual(caesar_cipher(plaintext, encrypt), answer)
        
        # Exception tests for when the encryption key is over 25 or below 0
        with self.assertRaises(ValueError):
            caesar_cipher("This should give an error if over 25", 26)
            caesar_cipher("This should give an error is less than 0", -1)

if __name__ == '__main__':
    unittest.main()
