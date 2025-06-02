import hashlib

def blake2(message):
    blake2_hash = hashlib.blake2b()
    blake2_hash.update(message)
    return blake2_hash.hexdigest()

def main():
    text = input("Nhap chuoi can bam: ")
    text_bytes = text.encode('utf-8')
    hashed_text = blake2(text_bytes)

    print("Chuoi van ban da nhap: ", text)
    print("Blake2 Hash:", hashed_text)

if __name__ == "__main__":
    main()