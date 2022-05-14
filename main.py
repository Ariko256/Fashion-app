from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.clock import Clock
import time
from ooth.authenticate import Auth
from kivymd.toast import toast
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from requests.exceptions import HTTPError
import json

SIZE = (280, 560)
Window.size = SIZE

auth = Auth().auth


def Toast_message(msg):
    return toast(text=f"{msg}", background=(77 / 255, 77 / 255, 77 / 255, 1))




class Tab(MDFloatLayout, MDTabsBase):
    pass


class FashionApp(MDApp):

    def __init__(self, **kwargs):
        super(FashionApp, self).__init__(**kwargs)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = 'Pink'
        self.theme_cls.primary_hue = '500'
    
    def show_dialog(self,msg):
        self.dialog = MDDialog(
            text=msg,
            buttons=[],
        )
        self.dialog.open()

   
    def build(self):
        return super().build()

    def on_start(self):
        self.carosel = self.root.ids.carousel
        img0 = self.root.ids.fitimage0
        img1 = self.root.ids.fitimage1
        img2 = self.root.ids.fitimage2

        url0 = "https://images.unsplash.com/photo-1546485299-dbe97f7454ed?ixid=MnwxMjA3fDB8MHx0b3BpYy1mZWVkfDI2fFM0TUtMQXNCQjc0fHxlbnwwfHx8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=60"
        url1 = "https://images.unsplash.com/photo-1461799821556-055545cf32dc?ixid=MnwxMjA3fDB8MHx0b3BpYy1mZWVkfDQzfFM0TUtMQXNCQjc0fHxlbnwwfHx8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=60"
        url2 = "https://images.unsplash.com/photo-1584598665938-079ecb78d906?ixid=MnwxMjA3fDB8MHx0b3BpYy1mZWVkfDE3fFM0TUtMQXNCQjc0fHxlbnwwfHx8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=60"

        img0.source = url0
        img1.source = url1
        img2.source = url2

        time.sleep(3)
        Clock.schedule_interval(self.slide_carosel, 4)

    def slide_carosel(self, args):
        self.carosel.load_next(mode="next")

    def Authenticate(self):
        email = self.root.ids.email_sighnup
        passwd = self.root.ids.password_sighnup
        confirm_passwd = self.root.ids.confirmpassword

        if email.text != "" and passwd.text != "" and confirm_passwd.text != "":

            if (passwd.text) == (confirm_passwd.text):

                if (len(passwd.text) >= int(6)):
                    try:
                        user = auth.create_user_with_email_and_password(
                            email.text, passwd.text)
                        Toast_message(f"user {email.text} has been created")
                        user = auth.sign_in_with_email_and_password(
                            email.text, passwd.text
                        )
                        auth.send_email_verification(user['idToken'])

                        email.text = ""
                        passwd.text = ""
                        confirm_passwd.text = ""

                    except HTTPError as e:
                        err = e.strerror
                        err_mod = json.loads(err)
                        print(err_mod["error"]["message"])
                        self.show_dialog(err_mod["error"]["message"])

                else:
                    Toast_message(
                        "password should be atleast 6 characters long  and should contain symbols")
                    passwd.text = ""
                    confirm_passwd.text = ""

            else:
                Toast_message("Passwords dont match")
                passwd.text = ""
                confirm_passwd.text = ""
                pass

        else:
            Toast_message("Fill in the blanks")

            pass

    def Login_user(self):
        email = self.root.ids.email
        password = self.root.ids.password

        if email.text != "" and password.text != "":

            try:
                signin = auth.sign_in_with_email_and_password(
                    email.text, password.text)

                self.root.current = "home_screen"
                Toast_message("Signed in succesfully")
                email.text = ""
                password.text = ""

            except HTTPError as e:
                err = e.strerror
                err_mod = json.loads(err)
                print(err_mod["error"]["message"])
                self.show_dialog(err_mod["error"]["message"])
                # Toast_message(err_mod["error"]["message"])

        else:
            Toast_message("Fill in the blanks")


if __name__ == "__main__":
    app = FashionApp()
    app.run()
