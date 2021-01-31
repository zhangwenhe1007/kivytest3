#!/usr/bin/python3

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFloatingActionButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
import speech_recognition as sr

recognizer = sr.Recognizer()

mic = sr.Microphone()

class App(MDApp):

    def build(self):
        screen = Screen()

        icon_btn = MDFloatingActionButton(icon='android',
                                          pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                          size_hint=(0.2, 0.25),
                                          on_press=self.get,
                                          on_release=self.show)

        screen.add_widget(icon_btn)

        return screen

    def get(self, obj):

        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            # recognize speech using Google Speech Recognition
            value = recognizer.recognize_google(audio)
            self.recorded = value

        except sr.UnknownValueError:
            self.recorded = ("Oops! Didn't catch that")

        except sr.RequestError as e:
            self.recorded = ("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))


    def show(self, obj):

        close_btn = MDFlatButton(text='Close',
                                 on_release=self.close_dialog)

        self.dialog = MDDialog(title='YES', text='It works maybe?!'+self.recorded,
                               size_hint=(0.7, 1),
                               buttons=[close_btn])

        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

App().run()
