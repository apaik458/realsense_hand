#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Point

def callback(data):
    rospy.loginfo("x: %.5f   y: %.5f   z: %.5f", data.x, data.y, data.z)
    
def test_topic():
    rospy.init_node('test_handDetect', anonymous=True)
    rospy.Subscriber("/hand_point_topic", Point, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    test_topic()
