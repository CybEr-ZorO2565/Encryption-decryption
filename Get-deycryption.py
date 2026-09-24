from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

KEY = b" "  # TODO: set your 16/24/32-byte AES key here


def encrypt_payload(plaintext: str, key: bytes = KEY) -> str:
    """
    Encrypts a plaintext string (usually a JSON body) and returns the
    base64 string to send as "encryptedRequest".
    """
    iv = get_random_bytes(12)
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode("utf-8"))
    blob = iv + ciphertext + tag
    return base64.b64encode(blob).decode("ascii")


def decrypt_payload(encrypted_b64: str, key: bytes = KEY) -> str:
    """
    Decrypts a base64 "encryptedRequest" / "encryptedPayload" string
    and returns the plaintext (usually JSON).
    """
    raw = base64.b64decode(encrypted_b64)
    iv = raw[:12]
    ciphertext = raw[12:-16]
    tag = raw[-16:]
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode("utf-8")


if __name__ == "__main__":
    # Quick self-test using the sample payload you captured
    choice = input("A or B: ")
    if choice == "A":
        print("Decrypting Mode")
        sample = input("Enter the encrypted value: ")
        plaintext = decrypt_payload(sample)
        print(plaintext)
    else:
        print("\nEncrypting Mode:")
        sample = input("Enter the encrypted value: ")
        print("Re-encrypted:", sample)