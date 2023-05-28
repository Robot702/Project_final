# -*- coding: utf-8 -*-
"""Navigation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dlNOHXqgVsWHEIKztGGy_IGtIyTzSVc1
"""

import rospy
from std_srvs.srv import Empty, EmptyResponse

def power_on(request):
    rospy.loginfo("Opening.")
    rospy.sleep(5)
    rospy.loginfo("It's on!!")
    return EmptyResponse()

def raise_the_temperature(request):
    rospy.loginfo("Working.")
    rospy.sleep(5)
    rospy.loginfo("Is reducing the temperature to 0 Celsius.")
    return EmptyResponse()

def power_off(request):
    rospy.loginfo("Power off.")
    rospy.sleep(5)
    rospy.loginfo("It's off!!")
    return EmptyResponse()

rospy.init_node('navigation_server')
power_on_service = rospy.Service('/Power_On', Empty, power_on)
raise_the_temperature_service = rospy.Service('/raise_the_temperature', Empty, raise_the_temperature)
power_off_service = rospy.Service('/Power_off', Empty, power_off)

rospy.spin()