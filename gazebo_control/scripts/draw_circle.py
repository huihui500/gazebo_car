#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist


if __name__=='__main__':
    rospy.init_node('sim_car_ctl', anonymous=True)
    
    pub_sim_car_ctl = rospy.Publisher("/cmd_vel", Twist, queue_size=20)
    r = rospy.Rate(20)
    ctl_cmd = Twist()
    # 线速度
    ctl_cmd.linear.x = 0.7
    # 角速度
    ctl_cmd.angular.z = 0.4
    while(True):
        pub_sim_car_ctl.publish(ctl_cmd)
        r.sleep()