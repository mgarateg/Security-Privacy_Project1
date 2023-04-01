from Crypto.Cipher import AES
import binascii, os

def encrypt_AES_GCM(msg, secretKey):
  aesCipher = AES.new(secretKey, AES.MODE_GCM)
  ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
  return (ciphertext, aesCipher.nonce, authTag)

def decrypt_AES_GCM(encryptedMsg, secretKey):
  (ciphertext, nonce, authTag) = encryptedMsg
  aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
  plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
  return plaintext

secretKey = os.urandom(32) # 256-bit random encryption key
print("Encryption key:", binascii.hexlify(secretKey))

msg = b'This is top secret!'
encryptedMsg = encrypt_AES_GCM(msg, secretKey)
print("\nEncrypted Message:", binascii.hexlify(encryptedMsg[0]))

decryptedMsg = decrypt_AES_GCM(encryptedMsg, secretKey)
print("\nDecrypted Message:", decryptedMsg)