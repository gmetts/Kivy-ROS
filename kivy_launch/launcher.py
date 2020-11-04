from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

import threading
import os
import time

def timer_thread():
    os.system('gnome-terminal -- bash -c "killall -9 roscore; killall -9 rosmaster;roslaunch kivy_ros_example timer.launch; exec bash"')

def keyboard_thread():
    os.system('gnome-terminal -- bash -c "killall -9 roscore; killall -9 rosmaster;roslaunch kivy_ros_example keyboard.launch; exec bash"')
    pass


class LaunchSelector(Widget):
    def __init__(self, **kwargs):
        super(LaunchSelector, self).__init__(**kwargs)

    def launch_timer(self):
        threading.Thread(target=timer_thread,daemon=True).start()

        App.get_running_app().stop()

    def launch_keyboard(self):
        threading.Thread(target=keyboard_thread,daemon=True).start()

        App.get_running_app().stop()
class LaunchApp(App):
    def build(self):
        
        return LaunchSelector()

if __name__ == '__main__':
    client_thread = threading.Thread(target=LaunchApp().run(),daemon=True)
    client_thread.start()

