cmake_minimum_required(VERSION 2.8.3)
project(serial_bridge)

add_compile_options(-std=c++11)
find_package(catkin REQUIRED COMPONENTS
  rospy
  rosserial
)

catkin_package(
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
