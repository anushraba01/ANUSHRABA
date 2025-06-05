from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b'pratikpa'

cipher = DES.new(key, DES.MODE_ECB)

plaintext = b'Institute of technical education'  


padded_text = pad(plaintext, DES.block_size)


ciphertext = cipher.encrypt(padded_text)
print(f'Encrypted: {ciphertext.hex()}')

decrypted_padded_text = cipher.decrypt(ciphertext)


decrypted_text = unpad(decrypted_padded_text, DES.block_size)
print(f'Decrypted: {decrypted_text.decode()}')