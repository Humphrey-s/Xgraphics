import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

    def build():
        return Label(text="Hell people of NewYork")


if __name__ == "__main__":
    MyApp.run()