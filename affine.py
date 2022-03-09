from utils import mod26_inv

class Affine:
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def enc(self, plain_text, key):
        cipher_text = ""
        for letter in plain_text.upper():
            if letter.isalpha():
                cipher = (key[0] * self.alphabet.index(letter) + key[1]) % 26
                cipher_text += self.alphabet[cipher]
            # else:
            #   cipher_text = cipher_text + letter
        return cipher_text

    def dec(self, cipher_text, key):
        plain_text = ""
        for letter in cipher_text.upper():
            if letter.isalpha():
                plain = (
                    mod26_inv(key[0]) * (self.alphabet.index(letter) - key[1])
                ) % 26
                plain_text += self.alphabet[plain]
        return plain_text

