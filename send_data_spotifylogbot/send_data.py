from encryptdecrypt import loadkeys,encrypt,generatekeys
from myfirebase import db,cred,app
import firebase_admin

def addaccount():
    privatekey,publickey=loadkeys()

    user_email=input("Enter your email: ")
    user_password=input("Enter your password: ")

    cipher=encrypt(user_password,publickey)

    users = db.collection('users').get()

    data={
        'email': user_email,
        'password': cipher,
        }

    try:
        send=db.collection('users').document().set(data)
        if send:
            return "SUCCESS"
    except:
        return "UNSUCCESSFULL"

Flag=True
# Main Menu code
while Flag:
    print('SELECT YOUR OPTIONS')
    print("1. ADD an Account")
    print("2. REMOVE an account")
    print("3. UPDATE details for an account")
    print("4. Exit")
    select=int(input("Enter your choice: "))

    if select==1:
        reply=addaccount()
    elif select==2:
        print('under development!! come back later')
    elif select==3:
        print('under development!! come back later')
    elif select==4:
        Flag=False
    else:
        print("invalid try again")