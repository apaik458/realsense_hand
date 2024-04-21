# realsense_nodes
Package for running MediaPipe hand detection on Intel RealSense camera

## Install
Clone repo
```bash
mkdir -p ~/catkin_ws/src && cd ~/catkin_ws/src
git clone https://github.com/apaik458/realsense_nodes.git
cd ~/catkin_ws && catkin_make
```
Install realsense-ros package
```bash
sudo apt-get install ros-noetic-realsense2-camera
```
Install Python dependencies
```bash
pip install -r requirements.txt
```

## Usage
Start realsense nodes
```bash
roslaunch realsense2_camera rs_camera.launch
```
Run realsense_nodes.py script to start hand detection program
```bash
rosrun realsense_nodes realsense_nodes.py
```

Run test_topic.py script to view geometry_msgs Point output
```bash
rosrun realsense_nodes test_topic.py
```
