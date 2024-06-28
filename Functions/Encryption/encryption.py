from cryptography.fernet import Fernet
def decrypt(*, cipherText):
    with open("Functions/Encryption/encryptionKey.txt","rb") as file:
        encryptionKey = file.read()
    cipher = Fernet(encryptionKey)
    return cipher.decrypt(cipherText).decode("UTF-8")

def encrypt(*, plaintext) -> str:
    with open("Functions/Encryption/encryptionKey.txt","rb") as file:
        encryptionKey = file.read()
    cipher = Fernet(encryptionKey)
    return cipher.encrypt(plaintext.encode("UTF-8"))

def generateKey():
    with open("Functions/Encryption/encryptionKey.txt","wb") as file:
        file.write(Fernet.generate_key())