import pyrebase
import os

API_KEY = str(os.environ.get('API_KEY'))
config = {
    "apiKey": API_KEY,
    "authDomain": "fashiondevsapp.firebaseapp.com",
    "projectId": "fashiondevsapp",
    "storageBucket": "fashiondevsapp.appspot.com",
    "messagingSenderId": "325766868054",
    "appId": "1:325766868054:web:f5d9c2ad3d9b507f9d5ff7",
    "measurementId": "G-9VCPKHG4FH",
    "databaseURL": ""
}


class Auth(object):

    def __init__(self, **kwargs):
        super(Auth, self).__init__(**kwargs)
        self.firebase = pyrebase.initialize_app(config)
        self.auth = self.firebase.auth()

    def send(self):
        print(self.auth.current_user)
