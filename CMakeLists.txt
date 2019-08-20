cmake_minimum_required(VERSION 2.8.3)
project(husarion_ros)

add_compile_options(-std=c++11)
find_package(catkin REQUIRED COMPONENTS
  rospy roscpp message_filters cv_bridge tf image_transport
)
find_package(OpenCV REQUIRED)

catkin_package(
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

add_executable(depth_clipping_node src/depth_clipping.cpp)

target_link_libraries(depth_clipping_node
  ${catkin_LIBRARIES}
)

add_executable(map_to_img_node src/map_to_img.cpp src/MapAsImageProvider.cpp)

target_link_libraries(map_to_img_node
  ${catkin_LIBRARIES}
  ${OpenCV_LIBRARIES}
)

install(DIRECTORY launch
	DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(DIRECTORY scripts
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  USE_SOURCE_PERMISSIONS
)

install(TARGETS depth_clipping_node map_to_img_node
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
