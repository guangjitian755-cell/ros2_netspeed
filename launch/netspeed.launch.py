#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Hikaru Yoshida
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions



def generate_launch_description():

    download = launch_ros.actions.Node(
        package='ros2_netspeed',
        executable='measur1',
    )

    upload = launch_ros.actions.Node(
        package='ros2_netspeed',
        executable='measur2',
    )

    output = launch_ros.actions.Node(
        package='ros2_netspeed',
        executable='output',
        output='screen'
    )

    return launch.LaunchDescription([download, upload, output])

