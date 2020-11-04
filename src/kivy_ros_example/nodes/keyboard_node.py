#!/usr/bin/env python3


import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

from keyboard_gui import KeyboardApp


if __name__ == '__main__':


    rospy.init_node('keyboard_gui')

    keyboard = KeyboardApp()
    keyboard.run()



