import hashlib

def calculate_sha256(input_string):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()


data_to_hash = input("nhap du lieu de hash bawng sha-256: ")
hash_value = calculate_sha256(data_to_hash)
print("Gia tri cua sha-256 hash la:", hash_value)

