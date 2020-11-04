#!/usr/bin/env python3


import rospy
from std_msgs.msg import Int64
from std_msgs.msg import Empty

i = Int64()

def reset_callback(dummy):
    i.data=0

if __name__ == '__main__':

    rospy.init_node('timer_node')
    r = rospy.Rate(1)

    reset_sub = rospy.Subscriber('timer_reset',Empty,callback=reset_callback)

    timer_pub = rospy.Publisher('timer_value',Int64,queue_size=1)

    i.data = 0

    while not rospy.is_shutdown():
        i.data = i.data + 1
        timer_pub.publish(i)
        r.sleep()



