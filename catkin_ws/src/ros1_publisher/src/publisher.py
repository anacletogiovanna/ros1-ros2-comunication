#!/usr/bin/env python

import rospy 
from geometry_msgs.msg import Twist
import random 


def publisher():
    pub = rospy.Publisher('/ros2_topic_subscribe', Twist, queue_size=10)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(1)

    values_twist = Twist()
        
    while not rospy.is_shutdown():

        values_twist.linear.x = random.uniform(0.0, 2.0)
        values_twist.linear.y = random.uniform(0.0, 2.0)
        values_twist.linear.z = random.uniform(0.0, 2.0)

        values_twist.angular.x = random.uniform(0.0, 2.0)
        values_twist.angular.y = random.uniform(0.0, 2.0)
        values_twist.angular.z = random.uniform(0.0, 2.0)
        
        rospy.loginfo(values_twist)
        pub.publish(values_twist)

        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass