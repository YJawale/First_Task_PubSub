#!/usr/bin/python3
import rospy
from std_msgs.msg import String 
to_send=""
rospy.init_node("MidMan")
#recieves, and sends the decrypted message
def original(msg):
    global to_send
    result = ""
    for i in range(len(msg.data)):
        result += chr((ord(msg.data[i]) + 23 - 97) % 26 + 97)
    print("got the encrypted stuff: "+msg.data)
    print("Now, decrypting")
    to_send=result  #decrypted message
listen_pubsub = rospy.Subscriber("/firstpub",String, original) #recieves from 'pub', under topic 'first_pub'
talker_pubsub=rospy.Publisher("/final",String,queue_size=1) #sends final string to 'sub' under topic '/final'
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    talker_pubsub.publish(to_send)
    rate.sleep()
rospy.spin() #kinda a loop, but in ros lol  