#!/usr/bin/env python
import rospy
import numpy as np
import roslib
import tf2_ros
from geometry_msgs.msg import Pose

if __name__ == '__main__':
	rospy.init_node('sync_data', anonymous=True)
	tfBuffer = tf2_ros.Buffer()
	listener = tf2_ros.TransformListener(tfBuffer)
	box = rospy.Publisher('box_pose', Pose,queue_size=1)
	#rospy.Subscriber("/tf", TFMessage, tf_callback)
	rate = rospy.Rate(10.0)

	while not rospy.is_shutdown():
		#print(listener.frameExists('/ar_marker_12'))
		try:
			trans = tfBuffer.lookup_transform('ar_marker_12', 'camera_rgb_optical_frame', rospy.Time(),rospy.Duration(1))
			print('yes')
		except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
			print('error')
			rate.sleep()
			continue
		tfBuffer.clear
		rate.sleep()
