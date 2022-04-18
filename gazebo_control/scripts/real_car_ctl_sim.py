#!/usr/bin/env python
import rospy
from gazebo_control.msg import RealCar_ctl
from geometry_msgs.msg import Twist
import serial
import time


Port = '/dev/ttyUSB0'
baudRate = 9600
ser = serial.Serial(Port, baudRate, timeout=1)
ser.flushInput()
ser.flushOutput()


def commandCallback(msg):
    print("receive:", msg)
    ##################
    # 通信协议
    # 控制映射
    #
    # num = chr(int(msg.data))
    # ser.write(num.encode())
    # strs = ser.readline().decode()
    # if (strs!=""):
        # print(strs)
    # time.sleep(1)

    
def main():
    rospy.init_node('real_car_ctl', anonymous=True)
    
    rospy.Subscriber("/cmd_vel", Twist, commandCallback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__=='__main__':
    main()
    # ser.close()