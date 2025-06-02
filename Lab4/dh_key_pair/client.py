from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

def generate_client_key_parameters(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def derive_shared_key(private_key, public_key):
    shared_key = private_key.exchange(public_key)
    return shared_key

def main():

    with open("server_public_key.pem", "rb") as f:
        server_public_key = serialization.load_pem_public_key(f.read())
    

    with open("server_parameters.pem", "rb") as f:
        parameters = serialization.load_pem_parameters(f.read())
    

    private_key, public_key = generate_client_key_parameters(parameters)
    
    shared_secret = derive_shared_key(private_key, server_public_key)
    
    print("Shared secret:", shared_secret.hex())

if __name__ == "__main__":
    main()