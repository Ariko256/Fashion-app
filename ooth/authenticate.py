import pyrebase
import os

API_KEY = os.environ.get('API_KEY')

config = {
    "apiKey": str(API_KEY),
    "authDomain": "authsystem-c8f34.firebaseapp.com",
    "projectId": "authsystem-c8f34",
    "databaseURL": "https://authsystem-c8f34-default-rtdb.firebaseio.com",
    "storageBucket": "authsystem-c8f34.appspot.com",
    "messagingSenderId": "182037227084",
    "appId": "1:182037227084:web:85eac5cb9911770d9176e9",
    "measurementId": "G-D2ZC6NE1SL"
}





class Auth(object):

    def __init__(self, **kwargs):
        super(Auth, self).__init__(**kwargs)
        self.firebase = pyrebase.initialize_app(config)
        self.auth = self.firebase.auth()

    def send(self):
        #self.auth.send_password_reset_email("arikojahn256@gmail.com")
        #self.auth.send_email_verification('J2A9LmjvxQgGJp3JBV6RnwbKVWD3')

        print(self.auth.current_user)



#Auth().send()
