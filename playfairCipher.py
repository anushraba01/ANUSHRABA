def create_playfair_matrix(key):
  
    key = key.upper().replace("J", "I")  
    
   
    key_chars = []
    for char in key:
        if char.isalpha() and char not in key_chars:
            key_chars.append(char)
    
    
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  
    for char in alphabet:
        if char not in key_chars:
            key_chars.append(char)
    
    # Create 5x5 matrix
    matrix = []
    for i in range(0, 25, 5):
        matrix.append(key_chars[i:i+5])
    
    return matrix

def find_position(matrix, char):
    
    char = char.upper()
    if char == 'J':
        char = 'I'
    
    for row_idx, row in enumerate(matrix):
        if char in row:
            col_idx = row.index(char)
            return row_idx, col_idx
    
    return -1, -1  

def prepare_message(message):
   
    message = message.upper().replace("J", "I")
    
    # Remove non-alphabetic characters
    message = ''.join(char for char in message if char.isalpha())
    
    # Split message into digraphs and handle repeated letters
    digraphs = []
    i = 0
    while i < len(message):
        if i == len(message) - 1:  # If last character is alone
            digraphs.append(message[i] + 'X')
            break
        
        if message[i] == message[i+1]:  # If two consecutive letters are the same
            digraphs.append(message[i] + 'X')
            i += 1
        else:
            digraphs.append(message[i] + message[i+1])
            i += 2
    
    return digraphs

def encrypt(message, key):
    matrix = create_playfair_matrix(key)
    digraphs = prepare_message(message)
    ciphertext = ""
    
    for digraph in digraphs:
        a, b = digraph[0], digraph[1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        
        # Same row
        if row_a == row_b:
            ciphertext += matrix[row_a][(col_a + 1) % 5]
            ciphertext += matrix[row_b][(col_b + 1) % 5]
        # Same column
        elif col_a == col_b:
            ciphertext += matrix[(row_a + 1) % 5][col_a]
            ciphertext += matrix[(row_b + 1) % 5][col_b]
        # Rectangle case
        else:
            ciphertext += matrix[row_a][col_b]
            ciphertext += matrix[row_b][col_a]
    
    return ciphertext

def decrypt(ciphertext, key):
    matrix = create_playfair_matrix(key)
    digraphs = []
    
    # Split ciphertext into digraphs
    for i in range(0, len(ciphertext), 2):
        digraphs.append(ciphertext[i:i+2])
    
    plaintext = ""
    
    for digraph in digraphs:
        a, b = digraph[0], digraph[1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        
        # Same row
        if row_a == row_b:
            plaintext += matrix[row_a][(col_a - 1) % 5]
            plaintext += matrix[row_b][(col_b - 1) % 5]
     
        elif col_a == col_b:
            plaintext += matrix[(row_a - 1) % 5][col_a]
            plaintext += matrix[(row_b - 1) % 5][col_b]
        
        else:
            plaintext += matrix[row_a][col_b]
            plaintext += matrix[row_b][col_a]
    
    
    if len(plaintext) > 0 and plaintext[-1] == 'X':
        plaintext = plaintext[:-1]
  
    clean_text = []
    i = 0
    while i < len(plaintext):
        if i < len(plaintext) - 1 and plaintext[i] == plaintext[i+1]:
            clean_text.append(plaintext[i])
            i += 2  # Skip the X that was between duplicates
        else:
            clean_text.append(plaintext[i])
            i += 1
    
    return ''.join(clean_text)

# Example usage
if __name__ == "__main__":
    key = "KEYWORD"
    message = "HELLO WORLD"
    
    print(f"Original message: {message}")
    
    encrypted = encrypt(message, key)
    print(f"Encrypted: {encrypted}")
    
    decrypted = decrypt(encrypted, key)
    print(f"Decrypted: {decrypted}")