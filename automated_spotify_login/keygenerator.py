import rsa

def generatekeys():
    (publickey,privatekey)=rsa.newkeys(1024)
    with open ('keys/publickey.pem','wb') as p:
        p.write(publickey.save_pkcs1('PEM'))
    
    with open('keys/privatekey.pem','wb') as p:
        p.write(privatekey.save_pkcs1('PEM'))

generatekeys()