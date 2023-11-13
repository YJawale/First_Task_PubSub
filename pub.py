#!/usr/bin/python3
#this line above tells ki 'aage ka code is written in python3, uske according compile kar'
import rospy
from std_msgs.msg import String 
rospy.init_node("The_Publisher")
#'rospy.init_node' is used to make new nodes in rospy
def change():
    result = ""
    name = input("Name input give")
    shift = 3 #encrypt by shifting 3 fwd
    for char in name:
        result += chr((ord(char) + shift - 97) % 26 + 97) 
    return result
talker_pub = rospy.Publisher("/firstpub",String,queue_size=1) #sending to pubsub
rate = rospy.Rate(1)
toSend=change()
while not rospy.is_shutdown():
    talker_pub.publish(toSend)
    rate.sleep()