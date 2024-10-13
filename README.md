# Open MCT / ROS 2 Telemetry Test (ROS 2)

This project should be used alongside the [Open MCT project](https://github.com/brandongasser/openmct-ros-test-openmct)

## About this Project

### Telemetry Source

Creates mock telemetry data and publishes it to a ROS topic called 'telemetry'.

### Telemetry Server

Opens a websocket server to allow Open MCT clients to connect. Subscribes to the 'telemetry' ROS topic and sends that data to the connected Open MCT clients.

## Running the Project

If ROS 2 Iron is not installed, install it using

```
$ sudo bash rosinstall.sh
```

Build the project (only needs to be done once)

```
$ colcon build
```

Source files

```
$ source /opt/ros/iron/setup.bash
$ source install/setup.bash
```

Run the project

```
$ ros2 launch launch/telemetry.launch.py
```