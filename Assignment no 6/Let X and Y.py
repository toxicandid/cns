# Let X and Y be two users. Develop a system where X wants to send a confidential

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import (Encoding,PrivateFormat,NoEncryption,PublicFormat,
)

# Step 1: Generate RSA key pairs for X and Y
def generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

x_private_key, x_public_key = generate_keys()  # X's keys
y_private_key, y_public_key = generate_keys()  # Y's keys

# Step 2: X encrypts the message for Y
def encrypt_message(message, public_key):
    return public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

# Step 3: X signs the message
def sign_message(message, private_key):
    message_hash = hashes.Hash(hashes.SHA256())
    message_hash.update(message)
    digest = message_hash.finalize()
    signature = private_key.sign(
        digest,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH,
        ),
        hashes.SHA256(),
    )
    return signature

message = b"Confidential message from X to Y"
encrypted_message = encrypt_message(message, y_public_key)
signature = sign_message(message, x_private_key)

# Step 4: Y decrypts the message
def decrypt_message(encrypted_message, private_key):
    return private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

decrypted_message = decrypt_message(encrypted_message, y_private_key)

# Step 5: Y verifies the signature and integrity
def verify_signature(message, signature, public_key):
    message_hash = hashes.Hash(hashes.SHA256())
    message_hash.update(message)
    digest = message_hash.finalize()
    try:
        public_key.verify(
            signature,
            digest,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )
        return True
    except:
        return False

is_signature_valid = verify_signature(decrypted_message, signature, x_public_key)

# Print Results
print("Original Message:", message)
print("Decrypted Message:", decrypted_message)
print("Is Signature Valid?", is_signature_valid)
