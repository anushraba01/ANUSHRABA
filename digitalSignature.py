import hashlib
import rsa

# Generate RSA keys (public and private)
(public_key, private_key) = rsa.newkeys(512)

# Simulated message/document sent from A to B
message = "This is a confidential message from A.".encode()

# Hashing the message
hashed = hashlib.sha256(message).digest()

# A signs the message (i.e., creates the digital signature)
signature = rsa.sign(message, private_key, 'SHA-256')

# B receives the message and signature, and verifies the signature
try:
    rsa.verify(message, signature, public_key)
    print("Authentication successful. The message is verified to be from A.")
except rsa.VerificationError:
    print("Authentication failed. The message may not be from A.")