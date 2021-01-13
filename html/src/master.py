#!/usr/bin/env python
from html.srv import test_srv
import rospy

def fun1(req):
    print('req is : {}'.format(req.num_req))
    return ["finish!"]

def main():
    rospy.init_node('server_test', anonymous = True)
    rospy.Service('test', test_srv, fun1)
    rospy.spin()

if __name__ == '__main__':
    main() 
