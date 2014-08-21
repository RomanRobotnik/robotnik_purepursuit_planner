cmake_minimum_required(VERSION 2.8.3)
project(robotnik_pp_msgs)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  actionlib
  actionlib_msgs
  geometry_msgs
  roscpp
  std_msgs
)

add_message_files(
   FILES
   goal.msg
)

add_action_files(DIRECTORY action FILES GoTo.action)

## Generate added messages and services with any dependencies listed here
generate_messages(DEPENDENCIES std_msgs actionlib_msgs geometry_msgs planner_msgs)


catkin_package(
#  LIBRARIES purepursuit_planner
  CATKIN_DEPENDS roscpp actionlib roscpp std_msgs actionlib_msgs geometry_msgs
#  DEPENDS system_lib
)



include_directories(
  ${catkin_INCLUDE_DIRS}
)


