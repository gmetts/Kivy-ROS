#!/usr/bin/env python3


import rospy

from timer_gui import TimerApp


if __name__ == '__main__':


    rospy.init_node('timer_gui')
    timer = TimerApp()
    timer.run()



