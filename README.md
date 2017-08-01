### prerequisite

ros kinetic

ros workspace (~/catkin_ws)

turtlebot

gazebo 7

anaconda2

theano, tensorflow, keras

openai gym

### 1. configure lidar sensor to kobuki 
lidar sensor should be configure in kobuki_description/urdf/kobuki.urdf.xacro

copy lidar_lite_v2_withRay.dae to kobuki_description/meshes

create sensors/ folder in kobuki_description/urdf

cd kobuki_description/urdf/sensors/

copy lidar_sensor.urdf.xacro to it

cd ..

modify kobuki.urdf.xacro 

### 2. run dqn in the env

Terminal 1:

cd ~/catkin_ws/src

git clone git@github.com:ha5ha6/myturtle_gazebo_test.git

cd ..

catkin_make

if python lib problem:

(the python-dateutil distribution was not found and is required by catkin-pkg)

export PYTHONPATH=~/anaconda2/lib/python2.7/site-packages:$PYTHONPATH

catkin_make

source devel/setup.bash

rospack list

(found myturtle_gazebo in ~/catkin_ws/src/myturtle_gazebo_test)

export PYTHONPATH=/usr/lib/python2.7/dist-packages:$PYTHONPATH

roslaunch myturtle_gazebo myturtle_simplemaze_brick.launch

Terminal 2:

export PYTHONPATH=~/catkin_ws/src/myturtle_gazebo_test:$PYTHONPATH

export PYTHONPATH=/usr/lib/python2.7/dist-packages:$PYTHONPATH

export PYTHONPATH=~/anaconda2/lib/python2.7/site-packages:$PYTHONPATH

cd ~/catkin_ws/src/myturtle_gazebo_test/script

python test_simplemaze_cvenv.py
