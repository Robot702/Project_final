# -*- coding: utf-8 -*-
"""Main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hLZ1G-TKY-C8rOJXM7leVZteSdJWsbIC
"""

import rospy
from std_srvs.srv import Empty

rospy.init_node('navigation_client')
rospy.wait_for_service('/raise_the_temperature')
rospy.wait_for_service('/Power_off')
rospy.wait_for_service('/Power_On')

raise_the_temperature = rospy.ServiceProxy('/raise_the_temperature', Empty)
power_off = rospy.ServiceProxy('/Power_off', Empty)
power_on = rospy.ServiceProxy('/Power_On', Empty)

raise_the_temperature()

power_off()

power_on()

power_off()