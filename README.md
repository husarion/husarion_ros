# husarion_ros

Husarion ros package contains some nodes specific for Husarion robots.

## Contents

There are four main launch files with names beginnig `rosbot_drivers`, these are for basic ROSbot controle, depending on ROSbot version and configuration.

- `rosbot_drivers.launch` is for ROSbot 2.0 connected to [cloud.husarion.com](cloud.husarion.com)
- `rosbot_driver_ofline.launch` is for ROSbot 2.0 with [disabled cloud connection](https://husarion.com/tutorials/other-tutorials/how-to-use-core2-ros-local-serial-offline/).
- `rosbot_drivers_pro.launch` is for ROSbot 2.0 PRO connected to [cloud.husarion.com](cloud.husarion.com)
- `rosbot_driver_pro_offline.launch` is for ROSbot 2.0 PRO with [disabled cloud connection](https://husarion.com/tutorials/other-tutorials/how-to-use-core2-ros-local-serial-offline/).

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
