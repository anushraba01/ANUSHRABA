def vigenere_encrypt(plaintext, key):

    plaintext = ''.join(char for char in plaintext.upper() if char.isalpha())
    key = ''.join(char for char in key.upper() if char.isalpha())
    
    if not key:
        return "Error: Key must contain at least one letter"
    
    repeated_key = (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]
    
    ciphertext = ""
    
    for p, k in zip(plaintext, repeated_key):
        # Convert letters to numbers (A=0, B=1, ..., Z=25)
        p_num = ord(p) - ord('A')
        k_num = ord(k) - ord('A')
        
        # Apply encryption formula and convert back to letter
        c_num = (p_num + k_num) % 26
        ciphertext += chr(c_num + ord('A'))
    
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    
    ciphertext = ''.join(char for char in ciphertext.upper() if char.isalpha())
    key = ''.join(char for char in key.upper() if char.isalpha())
    
    if not key:
        return "Error: Key must contain at least one letter"
    
    repeated_key = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
    
    plaintext = ""
    
    for c, k in zip(ciphertext, repeated_key):
        # Convert letters to numbers (A=0, B=1, ..., Z=25)
        c_num = ord(c) - ord('A')
        k_num = ord(k) - ord('A')
        
        # Apply decryption formula and convert back to letter
        p_num = (c_num - k_num) % 26
        plaintext += chr(p_num + ord('A'))
    
    return plaintext

# Example usage
if __name__ == "__main__":
    message = "HELLO WORLD"
    key = "KEY"
    
    print(f"Original message: {message}")
    
    encrypted = vigenere_encrypt(message, key)
    print(f"Encrypted: {encrypted}")
    
    decrypted = vigenere_decrypt(encrypted, key)
    print(f"Decrypted: {decrypted}")
    
    # Test with a longer message
    longer_message = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    print(f"\nOriginal longer message: {longer_message}")
    
    encrypted_longer = vigenere_encrypt(longer_message, key)
    print(f"Encrypted longer: {encrypted_longer}")
    
    decrypted_longer = vigenere_decrypt(encrypted_longer, key)
    print(f"Decrypted longer: {decrypted_longer}")


    '''remote user authentication basic telnet(router configuration)
enable
configure terminal
hostname R1
username admin privilege 15 secret Admin@123
username netops privilege 10 secret Net0ps!456
line vty 0 4
 transport input telnet
 login local
 exit
interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.0
 no shutdown
 exit
service password-encryption
end
write memory

(for switch)enable
configure terminal
hostname SW1
username admin privilege 15 secret Admin@123
username netops privilege 10 secret Net0ps!456
line vty 0 15
 transport input telnet
 login local
 exit
interface Vlan1
 ip address 192.168.1.2 255.255.255.0
 no shutdown
 exit
ip default-gateway 192.168.1.1
service password-encryption
end
write memory
'''

# Remote user authentication using SSH (router configuration)
'''enable
configure terminal
hostname R1
ip domain-name example.com
crypto key generate rsa general-keys modulus 2048
username admin privilege 15 secret Admin@123
username netops privilege 10 secret Net0ps!456
ip ssh version 2
ip ssh time-out 60
ip ssh authentication-retries 3
line vty 0 4
 transport input ssh
 login local
 exit
interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.0
 no shutdown
 exit
service password-encryption
end
write memory

(for switch)enable
configure terminal
hostname SW1
ip domain-name example.com
crypto key generate rsa general-keys modulus 2048
username admin privilege 15 secret Admin@123
username netops privilege 10 secret Net0ps!456
ip ssh version 2
ip ssh time-out 60
ip ssh authentication-retries 3
line vty 0 15
 transport input ssh
 login local
 exit
interface Vlan1
 ip address 192.168.1.2 255.255.255.0
 no shutdown
 exit
ip default-gateway 192.168.1.1
service password-encryption
end
write memory

(verification command)
show running-config | include username
show running-config | section line vty
show users
show ssh (for SSH configuration only)'''

''''standard access list
R2> enable
R2# configure terminal
R2(config)# access-list 10 permit host 192.168.1.5   # Allow only this PC
R2(config)# access-list 10 deny any                 # Block others
R2(config)# interface GigabitEthernet0/1           # Interface facing R1
R2(config-if)# ip access-group 10 in               # Apply inbound on R2
R2(config-if)# exit
R2(config)# exit


extended access list
R1> enable
R1# configure terminal
R1(config)# access-list 100 permit tcp host 192.168.1.5 host 10.0.0.5 eq 80  # Allow HTTP
R1(config)# access-list 100 permit tcp host 192.168.1.5 host 10.0.0.5 eq 21  # Allow FTP
R1(config)# access-list 100 deny ip any host 10.0.0.5                         # Block rest
R1(config)# interface GigabitEthernet0/0           # Interface facing PCs
R1(config-if)# ip access-group 100 out             # Apply outbound on R1
R1(config-if)# exit
R1(config)# exit
check access list
R1# show access-lists 100
R2# show access-lists 10

test connectivity
ping 10.0.0.5
telnet  10.0.0.5 80
telnet 10.0.0.5 21
'''
''' aaa username/password
Router> enable
Router# configure terminal

! Enable AAA globally
Router(config)# aaa new-model

! Define AAA server (TACACS+ example)
Router(config)# tacacs-server host 192.168.1.100 key MySecretKey

! Configure authentication method for login (use local if server fails)
Router(config)# aaa authentication login default group tacacs+ local

! Create a local fallback admin user (optional)
Router(config)# username admin privilege 15 secret Admin@123

! Apply AAA to VTY lines (remote access)
Router(config)# line vty 0 4
Router(config-line)# login authentication default
Router(config-line)# exit

! Apply AAA to console (optional)
Router(config)# line con 0
Router(config-line)# login authentication default
Router(config-line)# exit

verification
Router# show running-config | include aaa
Router# show tacacs-server
Router# show users
telnet 192.168.1.1



aaa for ssh 

outer> enable
Router# configure terminal

! Enable AAA (if not already done)
Router(config)# aaa new-model

! Configure TACACS+/RADIUS server
Router(config)# tacacs-server host 192.168.1.100 key MySecretKey

! Set AAA authentication for SSH
Router(config)# aaa authentication login SSH_AUTH group tacacs+ local

! Create local backup user
Router(config)# username sshadmin privilege 15 secret Ssh@123

! Configure SSH settings
Router(config)# ip domain-name example.com
Router(config)# crypto key generate rsa modulus 2048
Router(config)# ip ssh version 2

! Apply AAA to VTY lines for SSH-only access
Router(config)# line vty 0 4
Router(config-line)# transport input ssh
Router(config-line)# login authentication SSH_AUTH
Router(config-line)# exit

verification
Router# show ip ssh
Router# show running-config | include ssh
show aaa sessions

ssh -l username 192.168.1.1

Here are the *command sets* for configuring and verifying remote user authentication on a Cisco router using AAA with a username-password server (TACACS+/RADIUS) for both *basic access* and *SSH*:

---

### *1. AAA Authentication for Console/VTY Access (Username/Password)*
#### *Configuration Steps*
bash
Router> enable
Router# configure terminal

! Enable AAA globally
Router(config)# aaa new-model

! Define AAA server (TACACS+ example)
Router(config)# tacacs-server host 192.168.1.100 key MySecretKey

! Configure authentication method for login (use local if server fails)
Router(config)# aaa authentication login default group tacacs+ local

! Create a local fallback admin user (optional)
Router(config)# username admin privilege 15 secret Admin@123

! Apply AAA to VTY lines (remote access)
Router(config)# line vty 0 4
Router(config-line)# login authentication default
Router(config-line)# exit

! Apply AAA to console (optional)
Router(config)# line con 0
Router(config-line)# login authentication default
Router(config-line)# exit


#### *Verification Commands*
bash
# Check AAA configuration
Router# show running-config | include aaa
Router# show tacacs

# Test authentication (from a PC via Telnet/SSH)
C:\> telnet 192.168.1.1  # Enter AAA credentials when prompted


---

### *2. AAA Authentication for SSH (Secure Shell)*
#### *Configuration Steps*
bash
Router> enable
Router# configure terminal

! Enable AAA (if not already done)
Router(config)# aaa new-model

! Configure TACACS+/RADIUS server
Router(config)# tacacs-server host 192.168.1.100 key MySecretKey

! Set AAA authentication for SSH
Router(config)# aaa authentication login SSH_AUTH group tacacs+ local

! Create local backup user
Router(config)# username sshadmin privilege 15 secret Ssh@123

! Configure SSH settings
Router(config)# ip domain-name example.com
Router(config)# crypto key generate rsa modulus 2048
Router(config)# ip ssh version 2

! Apply AAA to VTY lines for SSH-only access
Router(config)# line vty 0 4
Router(config-line)# transport input ssh
Router(config-line)# login authentication SSH_AUTH
Router(config-line)# exit


#### *Verification Commands*
bash
# Verify SSH and AAA settings
Router# show ip ssh
Router# show running-config | include ssh
Router# show aaa sessions

# Test SSH from a PC (use TACACS+ credentials)
C:\> ssh -l username 192.168.1.1


---

### *Summary of Key Steps*
| *Task*                | *Commands*                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| *Enable AAA*          | aaa new-model                                                             |
| *Define TACACS+*      | tacacs-server host <IP> key <KEY>                                         |
| *Set Login Method*    | aaa authentication login <LIST> group tacacs+ local                       |
| *Local Fallback User* | username <name> privilege 15 secret <password>                            |
| *SSH Setup*           | ip domain-name, crypto key generate rsa, ip ssh version 2             |
| *Apply to VTY*        | line vty 0 4 + login authentication <LIST> + transport input ssh      |

Would you like a *Packet Tracer test procedure* for this setup? I can provide steps to validate AAA authentication with a simulated TACACS+ server.'''