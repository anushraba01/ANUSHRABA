from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

def generate_key():
    return get_random_bytes(32)  # 256-bit key

def encrypt(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct

def decrypt(iv, ct, key):
  try:
    iv_bytes = base64.b64decode(iv)
    ct_bytes = base64.b64decode(ct)
    cipher = AES.new(key, AES.MODE_CBC, iv_bytes)
    pt_bytes = unpad(cipher.decrypt(ct_bytes), AES.block_size)
    plaintext = pt_bytes.decode('utf-8')
    return plaintext
  except ValueError as e:
    return f"Decryption error: {e}"

key = generate_key()
iv, ciphertext = encrypt('Anushraba Pati', key)
plaintext = decrypt(iv, ciphertext, key)

print("Ciphertext:", ciphertext)
print("Plaintext:", plaintext)