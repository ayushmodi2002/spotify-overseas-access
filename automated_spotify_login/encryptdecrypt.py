import rsa


def loadkeys():
    print('Loading Keys........')
    with open ('keys/publickey.pem','rb') as p:
        public_key=rsa.PublicKey.load_pkcs1(p.read())
    
    with open('keys/privatekey.pem','rb') as p:
        private_key=rsa.PrivateKey.load_pkcs1(p.read())
    return private_key,public_key

def decrypt(ciphertext,key):
    print('decrypting password............')
    try:
        decrypted_text=rsa.decrypt(ciphertext,key).decode('utf-8')
        return decrypted_text
    except:
        print("Error decrypting password.")
