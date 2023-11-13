#!/usr/bin/python3
import rospy
from std_msgs.msg import String 
rospy.init_node("Final_output")
def original(msg):
    print(msg.data)
listen_sub = rospy.Subscriber("/final",String, original) #recieves from 'pubsub', under topic 'final'
rospy.spin() #kinda a loop, but in ros lol