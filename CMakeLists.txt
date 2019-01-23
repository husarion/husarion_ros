cmake_minimum_required(VERSION 2.8.3)
project(husarion_ros)

add_compile_options(-std=c++11)
find_package(catkin REQUIRED COMPONENTS
  rospy roscpp message_filters cv_bridge
)

catkin_package(
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(depth_clipping_node src/depth_clipping.cpp)

target_link_libraries(depth_clipping_node
  ${catkin_LIBRARIES}
)

install(DIRECTORY launch
	DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(DIRECTORY scripts
	DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(TARGETS depth_clipping_node
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
