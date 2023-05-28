import firebase_admin
from firebase_admin import credentials
# from firebase_admin import db
from firebase_admin import firestore


#fetch service account from firebase
cred=credentials.Certificate('firebase-credentials.json')

# intializing the app 
app=firebase_admin.initialize_app(cred)

db=firestore.client()

