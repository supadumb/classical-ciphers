import numpy as np
from utils import mod26_inv

class Hill:
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def enc(self, plain_text, key):
        cipher_text = ""
        # Ma trận khoá
        key_np = np.array(key)
        # Chạy vòng lặp để tách chuỗi thành từng cặp chữ rồi thực mã hoá
        for i in self.split_and_group_letters(plain_text):
            # thực hiện mã hoá theo phương trình e(x) = k*x
            cipher_code = np.mod(np.dot(i, key_np), 26)
            # chuyển đổi từng cặp mã ở trên thành từng cặp chữ cái
            cipher_text += self.alphabet[cipher_code[0]] + self.alphabet[cipher_code[1]]
        return cipher_text

    def dec(self, cipher_text, key):
        plain_text = ""
        # Tìm ma trận khoá nghịch đảo
        key_np = np.array(key)
        # 1.Tìm định thức nghịch đảo
        inv_det = mod26_inv(int(np.linalg.det(key_np)) % 26)
        # 2.Tính toán ma trận khoá nghịch đoả
        # Thực hiện nhân
        inv_key = np.dot(
            inv_det, [[key_np[1][1], -key_np[0, 1]], [-key_np[1][0], key_np[0, 0]]]
        )
        # Thực hiện mod 26
        inv_key = np.mod(inv_key, 26)
        # Chạy vòng lặp để tách chuỗi thành từng cặp chữ cái
        for i in self.split_and_group_letters(cipher_text):
            # thực hiện giải mã theo theo phương trình e(y) = k-1*y để lấy cặp mã
            plain_code = np.mod(np.dot(i, inv_key), 26)
            # chuyển đổi từng cặp mã ở trên thành từng cặp chữ cái
            plain_text += self.alphabet[plain_code[0]] + self.alphabet[plain_code[1]]
        return plain_text

    # đây là hàm thực hiện tách chữ, chuyển đổi chữ cái thành số và gộp thành từng ma trận 2x1
    def split_and_group_letters(self, inp):
        length = len(inp)
        inp = inp.upper()
        res = []
        if length % 2 == 0:
            for i in range(0, len(inp), 2):
                res.append(
                    np.array(
                        [self.alphabet.index(inp[i]), self.alphabet.index(inp[i + 1])]
                    )
                )
        return res

