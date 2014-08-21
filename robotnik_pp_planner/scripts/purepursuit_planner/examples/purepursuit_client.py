#! /usr/bin/env python

import roslib; roslib.load_manifest('purepursuit_planner')
import rospy
import time
# Brings in the SimpleActionClient
import actionlib
from geometry_msgs.msg import Pose2D
from robotnik_pp_msgs.msg import *

# Brings in the messages used by the purepursuit action, including the
# goal message and the result message.
#import purepursuit_planner.msg

def purepursuit_client():
	# Creates the SimpleActionClient, passing the type of the action
	# (GoTo) to the constructor.
	client = actionlib.SimpleActionClient('robotnik_pp_planner', GoToAction)

	# Waits until the action server has started up and started
	# listening for goals.
	client.wait_for_server()
	#g = GoToGoal(target = [goal(pose = Pose2D(0.0, 0.0, 0.0), speed = 0.2), goal(pose = Pose2D(2.0, 0.0, 0.0), speed = 0.2), goal(pose = Pose2D(3.0, -1.0, 0.0), speed = 0.2), goal(pose = Pose2D(4.0, -1.0, 0.0), speed = 0.2)])
	g1 = GoToGoal(target = [goal(pose = Pose2D(1.274, 0.097, 0.0), speed = 0.2), goal(pose = Pose2D(3.785, 0.048, 0.0), speed = 0.2)])
	# Creates a goal to send to the action server.
	#goal = purepursuit_planner.msg.GoToGoal(target=g)
	print 'Sending goal 1 and 2'
	# Sends the goal to the action server.
	client.send_goal(g1)
	#print 'Sleeping'
	time.sleep(2)
	g2 = GoToGoal(target = [goal(pose = Pose2D(6.599, 0.381, 0.0), speed = 0.2), goal(pose = Pose2D(7.623, -0.34, 0.0), speed = 0.2)])
	print 'Sending goal 3 and 4'
	client.send_goal(g2)
	#print 'Canceling goal'
	#client.cancel_goal()
	# Waits for the server to finish performing the action.
	client.wait_for_result()

	# Prints out the result of executing the action
	return client.get_result()  # A FibonacciResult

if __name__ == '__main__':
	try:
		# Initializes a rospy node so that the SimpleActionClient can
		# publish and subscribe over ROS.
		rospy.init_node('purepursuit_client_py')
		result = purepursuit_client()
		print 'Result: %d'%(result.route_result)
	except rospy.ROSInterruptException:
		print "program interrupted before completion"
