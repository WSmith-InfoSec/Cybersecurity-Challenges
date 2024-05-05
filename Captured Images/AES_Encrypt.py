from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

with open ("text.txt", "rb") as data:
    plaintext = data.read()

secret_key = get_random_bytes(16)

file_key = open("AES_key.txt", "wb")
file_key.write(secret_key)
file_key.close()

cipher_AES = AES.new(secret_key, AES.MODE_CFB)
cipher_text = cipher_AES.encrypt(plaintext)


file_out = open("AES_Encrypted.bin", "wb")
file_out.write(cipher_AES.iv)
file_out.write(cipher_text)
file_out.close()
