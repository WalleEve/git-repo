from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

# Set window background color (RGBA)
Window.clearcolor = (0.1, 0.1, 0.1, 1)  # Dark gray background

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        # Main layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Title Label
        title = Label(text="Login", font_size=32, color=(1, 1, 1, 1))
        layout.add_widget(title)

        # Username input
        self.username = TextInput(hint_text="Username", multiline=False, size_hint=(1, 0.2), background_color=(1, 1, 1, 0.8))
        layout.add_widget(self.username)

        # Password input
        self.password = TextInput(hint_text="Password", password=True, multiline=False, size_hint=(1, 0.2), background_color=(1, 1, 1, 0.8))
        layout.add_widget(self.password)

        # Login Button
        login_button = Button(text="Login", size_hint=(1, 0.3), background_color=(0.3, 0.6, 1, 1))
        login_button.bind(on_press=self.validate_credentials)
        layout.add_widget(login_button)

        self.add_widget(layout)

    def validate_credentials(self, instance):
        if self.username.text == "user" and self.password.text == "password":
            popup = Popup(title="Login Success", content=Label(text="Welcome!"), size_hint=(0.6, 0.4))
            popup.open()
        else:
            popup = Popup(title="Login Failed", content=Label(text="Invalid credentials"), size_hint=(0.6, 0.4))
            popup.open()


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        return sm

if __name__ == '__main__':
    MyApp().run()
