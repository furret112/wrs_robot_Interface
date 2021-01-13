#!/usr/bin/env python
import rospy
from html.srv import test_srv
from html.msg import my_msg 

msg = my_msg()


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)
    pass_msg_to_server(data.id)

def listener():
    rospy.init_node('relay', anonymous=True)
    rospy.Subscriber('Big_GG', my_msg, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def pass_msg_to_server(msg):
    rospy.wait_for_service('test')
    try:
        val = rospy.ServiceProxy('test', test_srv)
        resp = val(msg)
        print('{}'.format(resp.num_res))
    except rospy.ServiceException, e:
        print error

if __name__ == "__main__":

    listener()
