class Vigenere:
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def enc(self, plain_text, key, m):
        cipher_text = ""
        key = key.upper()
        run = 0
        for letter in plain_text.upper():
            if letter.isalpha():
                if run < m:
                    cipher = (
                        self.alphabet.index(letter) + self.alphabet.index(key[run])
                    ) % 26
                    cipher_text += self.alphabet[cipher]
                    run = run + 1
                else:
                    run = 0
                    cipher = (
                        self.alphabet.index(letter) + self.alphabet.index(key[run])
                    ) % 26
                    cipher_text += self.alphabet[cipher]
                    run = run + 1
            # else:
            #   cipher_text = cipher_text + letter
        return cipher_text

    def dec(self, cipher_text, key, m):
        plain_text = ""
        key = key.upper()
        run = 0
        for letter in cipher_text.upper():
            if letter.isalpha():
                if run < m:
                    cipher = (
                        self.alphabet.index(letter) - self.alphabet.index(key[run])
                    ) % 26
                    plain_text += self.alphabet[cipher]
                    run = run + 1
                else:
                    run = 0
                    cipher = (
                        self.alphabet.index(letter) - self.alphabet.index(key[run])
                    ) % 26
                    plain_text += self.alphabet[cipher]
                    run = run + 1
            # else:
            #   cipher_text = cipher_text + letter
        return plain_text
