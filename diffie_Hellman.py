
q = 157  # prime number
p = 5    # primitive root


a_private = 15  
b_private = 13  

# Public keys (to be exchanged over public channel)
yA = pow(p, a_private, q)  # A's public key
yB = pow(p, b_private, q)  # B's public key

# Shared secret key calculation
kA = pow(yB, a_private, q)  # Key computed by A
kB = pow(yA, b_private, q)  

print("Public key of A (yA):", yA)
print("Public key of B (yB):", yB)
print("Shared secret key computed by A (kA):", kA)
print("Shared secret key computed by B (kB):", kB)