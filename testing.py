from os import urandom
import blowfish
from operator import xor
import file as f
import key as k

data_path = input('enter data file path: ')
key = int(input('enter a fibonacci sequance number to generate the key: '))
cipher = blowfish.Cipher(k.generate_key(key))

data = f.read_file(data_path)


# increment by one counters
nonce = int.from_bytes(urandom(8), "big")
enc_counter = blowfish.ctr_counter(nonce, f = xor)
dec_counter = blowfish.ctr_counter(nonce, f = xor)

data_encrypted = b"".join(cipher.encrypt_ctr(data, enc_counter))
data_decrypted = b"".join(cipher.decrypt_ctr(data_encrypted, dec_counter))

f.write_to_file('encrypted.txt',data_encrypted)
f.write_to_file('decrypted.txt',data_decrypted)

assert data == data_decrypted
