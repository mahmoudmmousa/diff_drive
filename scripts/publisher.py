#!/usr/bin/env python3


import rospy
import roslib

from std_msgs.msg import Int16
from std_msgs.msg import Bool

def convert_bool_to_int(message):
    if message.data == True:
    	print("s7")
    	brake_state=1
    	brakemode.publish(brake_state)

        
    	
    elif message.data == False:
    	print("8lt")
    	brake_state=2
    	brakemode.publish(brake_state)
    	
  #  print(message.data)
    
    
rospy.init_node("publisher")
rospy.Subscriber('brakebool', Bool, convert_bool_to_int)

brakemode= rospy.Publisher('brake', Int16, queue_size=10)



#rate = rospy.Rate()

#while not rospy.is_shutdown():
#    brake_state = 1
 #   brakemode.publish(brake_state)
  #  rate.sleep()
    
rospy.spin()
