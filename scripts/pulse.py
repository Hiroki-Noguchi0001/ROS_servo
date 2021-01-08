#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def moter_pulse():
    rospy.init_node('pulse_pub')
    pub = rospy.Publisher('Pulse', Int32, queue_size=1)
    rate = rospy.Rate(0.5)
    pulse = 500
    while not rospy.is_shutdown():
        if(pulse >= 3000):
            pulse = 500

        pub.publish(pulse)
        pulse += 500 
        rate.sleep()

if __name__=='__main__':
    try:
        moter_pulse()
    except rospy.ROSInterruptException: pass


