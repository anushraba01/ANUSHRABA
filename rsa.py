

def power(base, expo, m):
    res = 1
    base = base % m
    while expo > 0:
        if expo & 1:
            res = (res * base) % m
        base = (base * base) % m
        expo = expo // 2
    return res

def modInverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return -1

# RSA Key Generation
def generateKeys():
    p = 7919
    q = 1009
    
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e, where 1 < e < phi(n) and gcd(e, phi(n)) == 1
    e = 0
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break
    d = modInverse(e, phi)

    return e, d, n

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Encrypt message using public key (e, n)
def encrypt(m, e, n):
    return power(m, e, n)

# Decrypt message using private key (d, n)
def decrypt(c, d, n):
    return power(c, d, n)

# Main execution
if __name__ == "__main__":
    
    e, d, n = generateKeys()
  
    print(f"Public Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")
   
    M = 123
    print(f"Original Message: {M}")

    C = encrypt(M, e, n)
    print(f"Encrypted Message: {C}")

    decrypted = decrypt(C, d, n)
    print(f"Decrypted Message: {decrypted}")