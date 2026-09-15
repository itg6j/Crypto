from hashlib import sha1
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util.number import inverse
p_hex = "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff"
g_hex = "0x02"
A_hex = "0x1c51690fc085f52ca9e9cbaca694949d19e6b7ae632daff88032c967b8f1243b9bc55b984a532d3580072dba8aa8d8c5d94224bb24254b6a2d6f13572edb29df4e229138d63e624c8b20436f3a9b916a053e62cff02545dcec90215948467d8c466c68b7286e483272c11bbb12acbabcc320c5cb58d3de5bea703cebcc807599ecbf8abe7f7c0024cad6bd21cc49554f855427294eed808e9308a99a3d15eede50d92a7227dc0387e23ea4f2b2f1b668d1f122b5a7962019533d27ca185efe2d"
B_hex = "0x2558c1c5ca11150bc24bd2c7e325f1811886a6ce407a587245bfa7890cd9d2474e81f77dce4f28be8658b4643324eaeb116ba40eee98eaf141383411f998c15789f2111c9369427b281d84442f6ab9d0f666313dbcdaab85d1d0b40cda1b0c26cad6b17ac939406935553c7d75c2bed22aedf18ae68df4ee806fd85e0650b761ba587797ce574811b7a4ce22397542a8a5c6417a4f8b27c0f51bded30f0916a47b2684f31bb18eb061fd021ee62c492f2750a74c8fff3ac6f5fd5e67d0a6fdfa"
iv_hex = "ba4bbd12fc6ee16435459dc7d42a5b26"
flag_hex = "4d2cf57488677e70d6f694ed4b763a6d7f0e0d44f01967551505e074f0f0afbf0030d8bf63e07f27b3b6766acd755636"
p = int(p_hex, 16)
g = int(g_hex, 16)
A = int(A_hex, 16)
B = int(B_hex, 16)
iv = bytes.fromhex(iv_hex)
ciphertext = bytes.fromhex(flag_hex)
g_inv = inverse(g, p)
a = (A * g_inv) % p
shared_secret = (a * B) % p
key = sha1(str(shared_secret).encode()).digest()[:16]
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
decrypted = cipher.decrypt(ciphertext)
try:
    print("Flag:", unpad(decrypted, AES.block_size).decode())
except Exception:
    print("Decrypted raw bytes:", decrypted)
