#!/usr/bin/env python
import rospy
import numpy as np
import roslib
import tf2_ros
import tf
from tf.msg import tfMessage
from geometry_msgs.msg import Pose
tfBuffer = tf2_ros.Buffer()
listener = tf2_ros.TransformListener(tfBuffer)
br = tf.TransformBroadcaster()

#when calibrated at inital position ar_12 is -0.122 -0.059 0.006 0.071 is the x offset for the line
def tf_callback(data):
	if(data.transforms[0].child_frame_id=='ar_marker_12'):
		trans = tfBuffer.lookup_transform('camera_rgb_optical_frame','ar_marker_12', rospy.Time(0))#target frame, source frame
#Which if applied to data, will transform data in the source_frame into the target_frame
		br.sendTransform((trans.transform.translation.x+0.122, trans.transform.translation.y, trans.transform.translation.z),
	(trans.transform.rotation.x,trans.transform.rotation.y,trans.transform.rotation.z,trans.transform.rotation.w),
				 rospy.Time.now(),
				 "box_pose",
				 "camera_rgb_optical_frame")
		print('ar_12',trans.transform.translation.x,trans.transform.translation.y,trans.transform.translation.z)
	elif(data.transforms[0].child_frame_id=='ar_marker_13'):
		trans = tfBuffer.lookup_transform('camera_rgb_optical_frame', 'ar_marker_13', rospy.Time(0))
		br.sendTransform((trans.transform.translation.x+0.059, trans.transform.translation.y, trans.transform.translation.z),(trans.transform.rotation.x,trans.transform.rotation.y,trans.transform.rotation.z,trans.transform.rotation.w),
				 rospy.Time.now(),
				 "box_pose",
				 "camera_rgb_optical_frame")

		print('ar_13',trans.transform.translation.x,trans.transform.translation.y,trans.transform.translation.z)
	elif(data.transforms[0].child_frame_id=='ar_marker_14'):
		trans = tfBuffer.lookup_transform('camera_rgb_optical_frame', 'ar_marker_14',rospy.Time(0))
		br.sendTransform((trans.transform.translation.x-0.006, trans.transform.translation.y, trans.transform.translation.z),	(trans.transform.rotation.x,trans.transform.rotation.y,trans.transform.rotation.z,trans.transform.rotation.w),
				 rospy.Time.now(),
				 "box_pose",
				 "camera_rgb_optical_frame")

		print('ar_14',trans.transform.translation.x,trans.transform.translation.y,trans.transform.translation.z)
	elif(data.transforms[0].child_frame_id=='ar_marker_17'):
		trans = tfBuffer.lookup_transform('camera_rgb_optical_frame', 'ar_marker_17', rospy.Time(0))
		br.sendTransform((trans.transform.translation.x-0.071, trans.transform.translation.y, trans.transform.translation.z),(trans.transform.rotation.x,trans.transform.rotation.y,trans.transform.rotation.z,trans.transform.rotation.w),
				 rospy.Time.now(),
				 "box_pose",
				 "camera_rgb_optical_frame")

		print('ar_17',trans.transform.translation.x,trans.transform.translation.y,trans.transform.translation.z)
	
if __name__ == '__main__':
	rospy.init_node('sync_data', anonymous=True)
	rospy.Subscriber("/tf", tfMessage, tf_callback)
	try:
		rospy.spin()				
	except:
		print('shutting down..')
