# pose_track
tracking the pose of toy with 4 markers even when few markers are occluded1

# How to use
Run the rosmaster
```
roscore
```
play the bag to test with the prerecorded bag file in bags/ folder
```
rosbag play bag2.bag
```
Run the pose track node 
``` 
python pose_track.py
```
Output in rviz:
Transform of box (box_pose) with respect to frame (camera_rgb_optical_frame) is visible
which has both pose and orientation of the box
