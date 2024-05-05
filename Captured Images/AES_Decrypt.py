
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

file_in =  open("encrypted_file", "rb")

iv = file_in.read(16)

cipher_text = file_in.read()
file_in.close()

file_key = open("file", "rb")

## read also the secret key
secret_key = file_key.read()
file_key.close()
## read also the tag

cipher_AES = AES.new(secret_key, AES.MODE_CFB, iv=iv)
decrypted_message = cipher_AES.decrypt(cipher_text)

retrieval = open("decrypted_message.txt", "wb")
retrieval.write(decrypted_message)
retrieval.close()

print(decrypted_message)
