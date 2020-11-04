from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.app import Builder

import rospy
import rospkg
from geometry_msgs.msg import Twist
from std_msgs.msg import String

import os
import time
import threading



class Keyboard(Widget):
    vel_text = StringProperty()
    test_pub = rospy.Publisher('test',String,queue_size=1) 
    def vel_callback(self,newVel):
        self.ids.VelLabel.text=str(newVel)

    def do_action(self):
        self.ids.VelLabel.text = 'test'
        self.test_pub.publish('test')




class KeyboardApp(App):

    def build(self):
        rospack = rospkg.RosPack()
        Builder.load_file(rospack.get_path('kivy_ros_example')+'/kivy/keyboard.kv')
        keyboard = Keyboard(vel_text = "Waiting on button press")
        vel_sub  = rospy.Subscriber('cmd_vel',Twist,keyboard.vel_callback)

        return keyboard
