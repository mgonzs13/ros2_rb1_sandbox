
cmake_minimum_required(VERSION 3.5)
project(rb1_sandbox)

find_package(ament_cmake REQUIRED)
find_package(rb1_gazebo REQUIRED)

install(
  DIRECTORY launch maps
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
