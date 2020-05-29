# husarion_ros

Husarion ros package contains some nodes specific for Husarion robots.

## Contents

There are two main launch files with names beginnig `rosbot_drivers`, these are for basic ROSbot control, depending on ROSbot version and configuration.

- `rosbot_drivers.launch` is for ROSbot 2.0
- `rosbot_drivers_pro.launch` is for ROSbot 2.0 PRO

## WiFi status

The `wifi.py` script is simple node which gets WiFi signal strength  of currently connected networks and publish it as `diagnostic_msgs/DiagnosticArray`.

### How to use

Node requires few python dependencies, install them with:

```
pip install python-wifi ifparser
```

Run as standard ROS node:

```
rosrun husarion_ros wifi.py
```
