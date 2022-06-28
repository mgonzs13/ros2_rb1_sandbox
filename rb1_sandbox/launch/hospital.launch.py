
import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import (
    IncludeLaunchDescription, SetEnvironmentVariable
)
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():

    aws_dir = get_package_share_directory("aws_robomaker_hospital_world")

    stdout_linebuf_envvar = SetEnvironmentVariable(
        "RCUTILS_LOGGING_BUFFERED_STREAM", "1")

    world = os.path.join(aws_dir, "worlds", "hospital.world")

    gazebo_nav2_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory("rb1_gazebo"),
                         "launch", "gazebo_nav2.launch.py")),
        launch_arguments={"slam": "True",
                          "world": world,
                          "initial_nav_pose_x": "0.0",
                          "initial_nav_pose_y": "10.0",
                          "initial_nav_pose_yaw": "-1.57",
                          "initial_gaz_pose_x": "0.0",
                          "initial_gaz_pose_y": "10.0",
                          "initial_gaz_pose_yaw": "-1.57"}.items())

    ld = LaunchDescription()

    ld.add_action(stdout_linebuf_envvar)
    ld.add_action(gazebo_nav2_cmd)

    return ld
