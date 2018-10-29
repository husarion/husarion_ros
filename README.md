# husarion_ros

Husarion ros package contains some nodes specific for Husarion robots.

## Serial bridge

The serial_bridge.py script is modified version of rosserial_python.

## WiFi status

This simple node gets WiFi signal strength  of currently connected networks and publish it as `diagnostic_msgs/DiagnosticArray`

### How to use

Node requires few python dependencies, install them with:

```
pip install python-wifi ifparser
```

Run as standard ROS node:

```
rosrun husarion_ros wifi.py
```
