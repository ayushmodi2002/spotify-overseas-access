import rsa

def loadkeys():
    with open ('keys/publickey.pem','rb') as p:
        public_key=rsa.PublicKey.load_pkcs1(p.read())
    
    with open('keys/privatekey.pem','rb') as p:
        private_key=rsa.PrivateKey.load_pkcs1(p.read())
    
    return private_key,public_key

def encrypt(message,key):
    return rsa.encrypt(message.encode('utf-8'),key)
