RSA Algorithm in Python

A small educational implementation of RSA encryption written in plain Python. It generates a key pair, encrypts a message with the public key and decrypts it again with the private key.

For learning only. Do not use this to protect real data!!

Features
Prime generation using the Miller-Rabin primality test
Key pair generation (default 1024 bits)
Modular inverse via the extended Euclidean algorithm
Encryption and decryption of text messages
Uses Python's secrets module for secure randomness
Requirements
Python 3.9 or newer
No external packages


Usage:

In the terminal you will be asked to type a message. The program then prints the keys and the start of the ciphertext, and asks whether you want to decrypt it.

Generating key pair...

Public key (e, n): ...
Private key (d, n): ...

Type in the message you want to encrypt: Hello
Ciphertext: [ ... ]
Do you want to decrypt the message? (y/n): y
Decrypted message: 'Hello'
How it works
Pick two large primes p and q (gen_prime, checked with is_prime).
Compute n = p * q and phi = (p - 1) * (q - 1).
Choose the public exponent e = 65537.
Compute the private exponent d, the inverse of e modulo phi (mod_inv, using ext_gcd).
Encrypt each character code m as c = m^e mod n.
Decrypt each value as m = c^d mod n.

The public key is (e, n) and the private key is (d, n).

Limitations
Each character is encrypted on its own with no padding, so the same letter always produces the same ciphertext. This is easy to attack.
Real-world RSA needs a padding scheme such as OAEP. Use a vetted library like cryptography for anything serious.
