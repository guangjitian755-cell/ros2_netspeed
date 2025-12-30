#!/bin/bash
set -xv
# SPDX-FileCopyrightText: 2025 Hikaru Yoshida
# SPDX-License-Identifier: BSD-3-Clause

dir="$1"
[ "$dir" = "" ] && dir="$HOME"

source /opt/ros/humble/setup.bash

cd $dir/ros2_ws

source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
colcon build
source install/setup.bash

timeout 60 ros2 launch ros2_netspeed netspeed.launch.py > /tmp/netspeed.log

grep -E '[0-9]+\.[0-9]+\s+[0-9]+\.[0-9]+' /tmp/netspeed.log
