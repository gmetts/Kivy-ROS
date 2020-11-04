from kivy.app import App, Builder
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.core.text import Label as CoreLabel

import rospy
import rospkg
from std_msgs.msg import Empty,Int64

import os
import time

class Timer(Widget):
    reset_pub = rospy.Publisher('timer_reset',Empty,queue_size=1)

    def timer_tick_callback(self,time):
        self.ids.TimerLabel.text = str(time.data)

    def do_action(self):
        self.reset_pub.publish(Empty())
        self.ids.TimerLabel.text = "0"


class TimerApp(App):
    def build(self):
        rospack = rospkg.RosPack()
        Builder.load_file(rospack.get_path('kivy_ros_example')+'/kivy/timer.kv')
        timer = Timer()
        vel_sub  = rospy.Subscriber('timer_value',Int64,timer.timer_tick_callback)
        return timer
