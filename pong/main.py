# main.py
# Omkar H. Ramachandran
# omkar.ramachandran@colorado.edu
#
# Pong tutorial
import kivy
kivy.require('1.0.9')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector

class PongGame(Widget):
    pass

class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    velocity = ReferenceListProperty(velocity_x,velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) * self.pos

class PongApp(App):
    def build(self):
        return PongGame()

if __name__=='__main__':
    PongApp().run()
