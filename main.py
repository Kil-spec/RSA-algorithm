import math
import secrets

def is_prime(n: int, k: int = 5) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n -1
    while d % 2 == 0:
       r += 1
       d //= 2

    for _ in range(k):
        a = secrets.randbelow(n - 3) + 2
        x = pow(a, d, n)
        if x == 1 or n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def gen_prime(bits: int) -> int:
    while True:
        can = (3 << (bits - 2)) | secrets.randbits(bits - 2) | 1
        if is_prime(can):
            return can

def ext_gcd(a: int, b: int):
    if a == 0:
        return b, 0, 1
    g, x1, y1, = ext_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y

def mod_inv(e: int, phi: int) -> int:
    gcd, x, _ = ext_gcd(e, phi)
    if gcd != 1:
        raise ValueError(f"{e} has no modular inverse")
    return x % phi

def gen_pair(bit_len: int = 1024):
#public key: e, n
#private key: d, n
    e = 65537 #public standard
    while True:
        p = gen_prime(bit_len // 2)
        q = gen_prime(bit_len // 2)
        if p == q:
            continue
        phi = (p - 1) * (q - 1)
        if math.gcd(e, phi) == 1:
            break

    n = p * q      
    d = mod_inv(e, phi)
    return (e, n), (d, n)

def encrypt(msg: str, public_key: tuple) -> list[int]:
    e, n = public_key

    cipher = [pow(ord(char), e, n) for char in msg] 
    return cipher

def decrypt(cipher: list[int], private_key: tuple) -> str:
    d, n = private_key

    plain = [chr(pow(char, d, n)) for char in cipher]
    return "".join(plain)


if __name__ == "__main__":
    print("Generating key pair...")
    public_key, private_key = gen_pair(1024)

    print(f"\nPublic key (e, n):\n e = {public_key[0]}\n n={public_key[1]}")
    print(f"\nPrivate key (d, n):\n d = {private_key[0]}, n = {private_key[1]}")

    msg = input("Type in the message you want to encrypt:")
    print(f"\nOriginal Message: '{msg}'")

    encrypted_msg = encrypt(msg, public_key)
    print(f"\nCiphertext: \n '{encrypted_msg[:3]}'")

    ask = str(input("Do you want to decrypt the message? (y/n)"))
    if ask == "y":
        decrypted_msg = decrypt(encrypted_msg, private_key)
        print(f"\nDecrypted message: '{decrypted_msg}'")
    else:
        print("The message stays encrypted!")
        
