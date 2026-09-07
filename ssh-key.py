import base64
import hashlib
import struct
def parse_ssh_rsa_public_key(ssh_key_string: str):
    parts = ssh_key_string.strip().split()
    key_type = parts[0]
    raw_b64 = parts[1]
    comment = parts[2] if len(parts) > 2 else "No comment"
    raw_bytes = base64.b64decode(raw_b64)
    offset = 0
    def read_field(data, offset):
        length = struct.unpack(">I", data[offset : offset + 4])[0]
        offset += 4
        field = data[offset : offset + length]
        offset += length
        return field, offset
    parsed_type, offset = read_field(raw_bytes, offset)
    e_bytes, offset = read_field(raw_bytes, offset)
    n_bytes, offset = read_field(raw_bytes, offset)
    e = int.from_bytes(e_bytes, byteorder="big")
    n = int.from_bytes(n_bytes, byteorder="big")
    fp_sha256 = base64.b64encode(hashlib.sha256(raw_bytes).digest()).decode(
        "utf-8"
    )
    fp_md5 = ":".join(f"{b:02x}" for b in hashlib.md5(raw_bytes).digest())
    print("=" * 60)
    print("SSH RSA Public Key Details")
    print("=" * 60)
    print(f"Key Type: {parsed_type.decode('utf-8')}")
    print(f"Comment:  {comment}")
    print(f"Key Size: {n.bit_length()} bits")
    print("\n--- 1. Public Exponent (e) ---")
    print(f"Decimal: {e}")
    print("\n--- 2. Modulus (n) ---")
    print(f"Decimal:\n{n}")
    print("\n--- 3. Fingerprints ---")
    print(f"SHA256:  SHA256:{fp_sha256.rstrip('=')}")
    print(f"MD5:     MD5:{fp_md5}")
    print("=" * 60)
bruce_ssh_key = (
    "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCtPLqba+GFvDHdFVs1Vvdk56cKqqw5cdomlu034666UsoFIqkig8H5kNsNefSpaR/iU7G0ZKCiWRRuAbTsuHN+Cz526XhQvzgKTBkTGYXdF/WdG/6/umou3Z0+wJvTZgvEmeEclvitBrPZkzhAK1M5ypgNR4p8scJplTgSSb84Ckqul/Dj/Sh+fwo6sU3S3j92qc27BVGChpQiGwjjut4CkHauzQA/gKCBIiLyzoFcLEHhjOBOEErnvrRPWCIAJhALkwV2rUbD4g1IWa7QI2q3nB0nlnjPnjjwaR7TpH4gy2NSIYNDdC1PZ8reBaFnGTXgzhQ2t0ROBNb+ZDgH8Fy+KTG+gEakpu20bRqB86NN6frDLOkZ9x3w32tJtqqrJTALy4Oi3MW0XPO61UBT133VNqAbNYGE2gx+mXBVOezbsY46C/V2fmxBJJKY/SFNs8wOVOHKwqRH0GI5VsG1YZClX3fqk8GDJYREaoyoL3HKQt1Ue/ZW7TlPRYzAoIB62C0= bschneier@facts"
)
parse_ssh_rsa_public_key(bruce_ssh_key)
