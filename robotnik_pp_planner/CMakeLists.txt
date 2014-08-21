cmake_minimum_required(VERSION 2.8.3)
project(robotnik_pp_planner)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  nav_msgs
  roscpp
  std_msgs
  tf
  diagnostic_updater
  robotnik_pp_msgs
  ackermann_msgs
  interactive_markers
  visualization_msgs
  std_srvs
  actionlib
)


catkin_python_setup()

catkin_package(
  INCLUDE_DIRS include
#  LIBRARIES purepursuit_planner
  CATKIN_DEPENDS roscpp actionlib nav_msgs roscpp std_msgs tf geometry_msgs robotnik_pp_msgs ackermann_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########


include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)


## Declare a cpp executable
add_executable(robotnik_pp_planner_node src/purepursuit_planner.cpp src/Component.cc)

## Add cmake target dependencies of the executable/library
## as an example, message headers may need to be generated before nodes
add_dependencies(robotnik_pp_planner_node purepursuit_planner_generate_messages_cpp)

## Specify libraries to link a library or executable target against
target_link_libraries(robotnik_pp_planner_node
   ${catkin_LIBRARIES}
)

#############
## Install ##
#############


install(PROGRAMS
   scripts/purepursuit_planner/path_marker.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
 )


