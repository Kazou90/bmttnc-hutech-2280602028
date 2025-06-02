from Crypto.Hash import SHA3_256

def sha3(message):
    hash = SHA3_256.new()
    hash.update(message) 
    return hash.hexdigest() 

def main():
    text = input("Nhap chuoi can bam: ") 
    text_bytes = text.encode('utf-8')  
    hashed_text = sha3(text_bytes) 

    print("Chuoi van ban da nhap: ", text)
    print("SHA-3 Hash:", hashed_text)  

if __name__ == "__main__":
    main()
