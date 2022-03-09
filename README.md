# Classical Cryptography Application 
## 📗 Enviroment and Requirements
1. Python version: `Python 3.9.6`
2. Before run the codes above, need install these modules below  via `pip` command: `python pip install`
```bash
numpy==1.22.2
```
## 🧰 Installation
```bash
git clone https://github.com/kizu08/classical-ciphers
cd classical-ciphers
```
## 🌍 Quick start
This repo is about some `classical ciphers` implemented in `python`, and interact theme via the `CLI`
### [1. Affine Cipher](https://en.wikipedia.org/wiki/Affine_cipher) 
Example:
```python
from affine import Affine

affine = Affine()

print(affine.enc("It is nice today", [7, 3]))
print(affine.dec("ZFYBALOVKLOPFY", [7, 11]))
```
### [2. Vigenere Cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) 
Example:
```python
from vigenere import Vigenere

vigenere = Vigenere()

print(vigenere.enc("Information security", "cipher", 6))
print(vigenere.dec("KVUVVDCBXVRJGKJYMKA", "cipher", 6))
```
### [3. Hill Cipher](https://en.wikipedia.org/wiki/Hill_cipher)
Example:
```python
from hill import Hill

hill = Hill()
key = [[5, 8], [12, 7]]
plaintxt = "GOOD"
ciphertxt = hill.enc(plain_text=plaintxt, key=key)
print(ciphertxt)
```
>these code is work with key size is Matrix 2x2

