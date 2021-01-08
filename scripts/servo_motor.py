#!/usr/bin/env python3
import rospy
import pigpio
from std_msgs.msg import Int32
GPIO_PIN = 4
pi = pigpio.pi()

def callback(pulse):
    print('Subscriber_palse = %d' %pulse.data)
    pi.set_servo_pulsewidth(GPIO_PIN, pulse.data)

if __name__ == "__main__":
    rospy.init_node('servo_motor_sub')
    sub = rospy.Subscriber('Pulse', Int32, callback)
    rospy.spin()
