# rosserial_husarion

The rosserial_husarion package is modified version of rosserial_python.

# WiFi status

This simple node gets WiFi signal strength  of currently connected networks and publish it as `diagnostic_msgs/DiagnosticArray`

## How to use

Node requires few python dependencies, install them with:

```
pip install python-wifi ifparser
```

Run as standard ROS node:

```
rosrun rosserial_husarion wifi.py
```
